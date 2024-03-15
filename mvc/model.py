from alpha_vantage.cryptocurrencies import CryptoCurrencies
import pandas as pd
import numpy as np

from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM, Dropout
from keras.metrics import Accuracy
import tensorflow as tf

import datetime
import os

np.random.seed(42)
tf.random.set_seed(42)

class Model:
    def __init__(self) -> None:
        self.__theme = "dark"
        self.__cache_filename = './cache/btc_daily.csv'
        self.__btc_daily = pd.DataFrame()
        self.predictions = []   

    #private methods:
    def __load_cache(self) -> None | pd.DataFrame:
        try:
                return pd.read_csv(self.__cache_filename, index_col=0, parse_dates=True)
        except (IOError, FileNotFoundError):
            return None

    def __save_cache(self, data: pd.DataFrame) -> None:
        data.to_csv(self.__cache_filename)

    def clear_cache(self, path: str) -> None:
        with open(path, 'w'):
            pass
        os.remove('./cache/lstm_model.h5')

    def _is_valid_cache(self) -> bool:
        data = self.__load_cache()

        if (not isinstance(data, pd.DataFrame) or data.empty):
            return False  
        
        cache_date = data.index[-1].date()
        print(cache_date)
        now = datetime.datetime.today() - datetime.timedelta(days=1)

        return now.date() == cache_date

    def __prepare_data(self) -> None:
        columns = ['1b. open (USD)', '2b. high (USD)', '3b. low (USD)', '4b. close (USD)', '5. volume']
        columns_for_drop = ['1a. open (CNY)', '2a. high (CNY)', '3a. low (CNY)', '4a. close (CNY)', '6. market cap (USD)']

        self.__btc_daily.index = pd.to_datetime(self.__btc_daily.index)
        self.__btc_daily.drop(columns=columns_for_drop, inplace=True)
        self.__btc_daily.sort_index(inplace=True)

        for column in columns:
            self.__btc_daily[column] = pd.to_numeric(self.__btc_daily[column])

        self.__save_cache(self.__btc_daily)

    def __pre_train(self, window_size: int) -> np.array:
        series = self.__btc_daily['4b. close (USD)']
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(np.array(series).reshape(-1, 1))

        X, y = [], []
        for i in range(window_size, len(series)):
            X.append(scaled_data[i - window_size:i, 0])
            y.append(scaled_data[i, 0])

        X, y = np.array(X), np.array(y)
        X = np.reshape(X, (X.shape[0], X.shape[1], 1))

        return X, y, scaler

    #public methods:
    @property
    def theme(self) -> str:
        return self.__theme
    
    @theme.setter
    def theme(self, value: str) -> None:
        self.__theme = value

    def get_crypto_data(self) -> None:
        if (self._is_valid_cache()):
            self.__btc_daily = self.__load_cache() 
            return None

        btc_curr = CryptoCurrencies(key=os.getenv("API_KEY"), output_format='pandas')
        btc_daily, _ = btc_curr.get_digital_currency_daily(symbol='BTC', market='CNY')
        self.__btc_daily = pd.DataFrame.from_dict(btc_daily);
    
        self.__prepare_data()
    
    def train_lstm_model(self, window_size: int = 10) -> None:
        try:
            if (self.__btc_daily.empty):
                raise ValueError('An empty dataset. Have you loaded it firstly before start working?')

            if (os.path.exists('./cache/lstm_model.h5')):
                return None

            x_train, y_train, _ = self.__pre_train(window_size)

            x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

            model = Sequential()
            model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
            # model.add(Dropout(0.2))
            model.add(LSTM(50, return_sequences=True))
            # model.add(Dropout(0.2))
            model.add(LSTM(50))
            # model.add(Dropout(0.2))
            model.add(Dense(1))

            model.compile(optimizer='adam', loss='mean_squared_error')
            model.fit(x_train, y_train, epochs=15, batch_size=64)

            model.save('./cache/lstm_model.h5')
        except ValueError as val_e:
            print(str(val_e))

    def predict_model(self, num_days: int, window_size: int = 10) -> list:
        _, _, scaler = self.__pre_train(window_size)
        series = self.__btc_daily['4b. close (USD)'].values

        series_scaled = scaler.transform(series.reshape(-1, 1))

        X_pred = []
        for i in range(len(series_scaled) - window_size):
            X_pred.append(series_scaled[i:i + window_size])

        X_pred = np.array(X_pred)

        model = load_model('./cache/lstm_model.h5')

        predictions = []
        last_window = X_pred[-1] 

        for _ in range(num_days):
            last_scaled = np.expand_dims(last_window, axis=0)
            prediction_scaled = model.predict(last_scaled)
            prediction = scaler.inverse_transform(prediction_scaled)[0][0]
            predictions.append(prediction)
            
            last_window = np.append(last_window[1:], prediction_scaled, axis=0)

        return predictions

    def get_actual_data(self) -> tuple:
        actual_prices = self.__btc_daily['4b. close (USD)'].values
        timestamps = self.__btc_daily.index

        return actual_prices, timestamps


