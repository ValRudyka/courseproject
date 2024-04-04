from alpha_vantage.cryptocurrencies import CryptoCurrencies

import pandas as pd
import numpy as np
import os
from datetime import datetime

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM, Dropout

from fpdf import FPDF
import matplotlib.pyplot as plt

# PDF usage
class PDF(FPDF):
    def write_to_pdf(self, words: str) -> None:    
        self.set_text_color(r=0, g=0, b=0)
        self.set_font('Helvetica', '', 12)

        self.write(5, words)

    def create_title(self, title: str) -> None:
        self.set_font('Helvetica', 'b', 12)
        self.ln(40) # ln means line break

        self.write(5, title)
        self.ln(10)

        self.set_font('Helvetica', '', 14)
        self.set_text_color(r=128, g=128, b=128)
        today = datetime.today().strftime('%d/%m/%Y')
        self.write(4, today)

        self.ln(10)

# Business logic
class Model:
    def __init__(self) -> None:
        self.__theme = "dark"
        self.__btc_daily = pd.DataFrame()
        self.__predictions = []

    # Private methods:
    @property
    def __actual_values(self) -> np.ndarray:
        return self.__btc_daily['4b. close (USD)'].values

    @property
    def __actual_timestamps(self) -> pd.Index:
        return self.__btc_daily.index

    def __load_cache(self, path: str) -> None | pd.DataFrame:
        try:
            return pd.read_csv(path, index_col=0, parse_dates=True)
        except (IOError, FileNotFoundError):
            return None

    def _is_valid_cache(self) -> bool:
        data = self.__load_cache(os.getenv('BTC_CACHE_PATH'))

        if not isinstance(data, pd.DataFrame) or data.empty:
            return False  

        cache_date = data.index[-1].date()
        now = datetime.now()

        return now.date() == cache_date

    def __prepare_data(self) -> None: 
        """Prepares data for future usage in prediction"""
        columns_for_drop = ['1a. open (CNY)', '2a. high (CNY)', '3a. low (CNY)', '4a. close (CNY)', '6. market cap (USD)']

        self.__btc_daily.index = pd.to_datetime(self.__btc_daily.index)
        self.__btc_daily.drop(columns=columns_for_drop, inplace=True)
        self.__btc_daily.sort_index(inplace=True)

        self.save_cache(os.getenv('BTC_CACHE_PATH'))

    def __pre_train(self, window_size: int) -> tuple:
        """Prepares data for training, using MinMaxScaler to ease the train process 
            Receives: window_size - size of data which will be used for training
            Returns: tuple with X, y values and scaler
        """
        series = self.__actual_values
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(np.array(series).reshape(-1, 1))

        X, y = [], []
        for i in range(window_size, len(series)):
            X.append(scaled_data[i - window_size:i, 0])
            y.append(scaled_data[i, 0])

        X, y = np.array(X), np.array(y)
        X = np.reshape(X, (X.shape[0], X.shape[1], 1))

        return X, y, scaler

    # Public methods:
    @property
    def theme(self) -> str:
        return self.__theme
    
    @theme.setter
    def theme(self, value: str) -> None:
        self.__theme = value

    # working with cache
    def save_cache(self, path: str, extension: str = 'csv') -> None:
        if self.__btc_daily.empty:
            raise Exception('Have you loaded data before saving dataset?')
        
        if extension == 'csv':
            self.__btc_daily.to_csv(path)
        else:
            self.__btc_daily.to_excel(path)

    def clear_cache(self, path: str) -> None:
        with open(path, 'w'):
            pass

    # working with data
    def get_crypto_data(self) -> None:
        if self._is_valid_cache():
            self.__btc_daily = self.__load_cache(os.getenv('BTC_CACHE_PATH')) 
            return None
        try:
            btc_curr = CryptoCurrencies(key=os.getenv("API_KEY"), output_format='pandas')
            btc_daily, _ = btc_curr.get_digital_currency_daily(symbol='BTC', market='CNY')
            self.__btc_daily = pd.DataFrame.from_dict(btc_daily)
        except Exception:
            raise ValueError("There was an error during fetching data")
        
        self.__prepare_data()

    def train_lstm_model(self, window_size: int = 10) -> None:
        try:
            if self.__btc_daily.empty:
                raise ValueError('An empty dataset. Have you loaded it firstly before start working?')
            
            X, y, _ = self.__pre_train(window_size)
            X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

            model = Sequential()
            model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
            model.add(Dropout(0.2))
            model.add(LSTM(50, return_sequences=True))
            model.add(Dropout(0.2))
            model.add(Dense(1))
            model.add(LSTM(50))
            model.add(Dense(1))

            model.compile(optimizer='adam', loss='mean_squared_error')

            model.fit(X_train, y_train, epochs=50, batch_size=10, validation_data=(X_val, y_val))
            model.save(os.getenv('MODEL_CACHE_PATH'))
        except ValueError as val_e:
            raise ValueError(val_e)

    def predict_model(self, num_days: int, window_size: int = 10) -> None:
        _, _, scaler = self.__pre_train(window_size)
        series = self.__btc_daily['4b. close (USD)'].values

        series_scaled = scaler.transform(series.reshape(-1, 1))

        X_pred = []
        for i in range(len(series_scaled) - window_size):
            X_pred.append(series_scaled[i:i + window_size])

        X_pred = np.array(X_pred)
                
        model = load_model(os.getenv('MODEL_CACHE_PATH'))

        predictions = []
        last_window = X_pred[-1] 

        for _ in range(num_days):
            last_scaled = np.expand_dims(last_window, axis=0)
            prediction_scaled = model.predict(last_scaled)
            prediction = scaler.inverse_transform(prediction_scaled)[0][0]
            predictions.append(prediction)
            
            last_window = np.append(last_window[1:], prediction_scaled, axis=0)

        self.__predictions = predictions
        print(self.__predictions)

    def generate_line_chart(self, canvas = object, filename: str = "", isPDF: bool = False) -> None:
        ax = plt.subplot() if isPDF else canvas
        
        x_pred = pd.date_range(start=self.__actual_timestamps[-1], periods=len(self.__predictions)+1, freq='D')[1:]
        ax.clear()
        ax.plot(self.__actual_timestamps, self.__actual_values, color='r', label='Actual prices')
        ax.plot(x_pred, self.__predictions, color='b', label='Predicted prices')
        
        ax.set_title('BTC prices comparison')
        ax.set_xlabel('Date')
        ax.set_ylabel('Prices (USD)')
        ax.legend()

        if isPDF:
            plt.savefig(filename, dpi=500, orientation='landscape')

    def generate_area_chart(self, canvas = object, filename: str = "", isPDF: bool = False) -> None:
        ax = plt.subplot() if isPDF else canvas
        
        x_pred = pd.date_range(start=self.__actual_timestamps[-1], periods=len(self.__predictions)+1, freq='D')[1:]
        ax.clear()
        ax.plot(self.__actual_timestamps, self.__actual_values, color='r', label='Actual prices')
        ax.fill_between(self.__actual_timestamps, self.__actual_values, color='r', alpha=0.3)
        ax.plot(x_pred, self.__predictions, color='b', label='Predicted prices')
        ax.fill_between(x_pred, self.__predictions, color='b', alpha=0.3)
        
        ax.set_title('BTC prices comparison')
        ax.set_xlabel('Date')
        ax.set_ylabel('Prices (USD)')
        ax.legend()

        if isPDF:
            plt.savefig(filename, dpi=500, orientation='landscape')

    def generate_scatter_plot(self, canvas = object, filename: str = "", isPDF: bool = False) -> None:
        ax = plt.subplot() if isPDF else canvas

        x_pred = pd.date_range(start=self.__actual_timestamps[-1], periods=len(self.__predictions)+1, freq='D')[1:]
        ax.clear()
        ax.scatter(self.__actual_timestamps, self.__actual_values, color='r', label='Actual prices')
        ax.scatter(x_pred, self.__predictions, color='b', label='Predicted prices')

        ax.set_title('BTC prices Actual vs Predicted')
        ax.set_xlabel('Date')
        ax.set_ylabel('Prices (USD)')
        ax.legend()
        ax.grid(True)

        if isPDF:
            plt.savefig(filename, dpi=500, orientation='landscape')