from alpha_vantage.cryptocurrencies import CryptoCurrencies
import pandas as pd
import datetime
import os


class Model:
    def __load_cache(self) -> None | pd.DataFrame:
        try:
                return pd.read_csv(self.cache_filename, index_col=0, parse_dates=True)
        except (IOError, FileNotFoundError):
            return None

    def __save_cache(self, data: pd.DataFrame) -> None:
        data.to_csv(self.cache_filename)

    def clear_cache(self) -> None:
        with open(self.cache_filename, 'w'):
            pass

    def _is_valid_cache(self) -> bool:
        data = self.__load_cache()

        if (not isinstance(data, pd.DataFrame) or data.empty):
            return False  
        
        cache_date = data.index[-1].date()
        print(cache_date)
        now = datetime.datetime.now().date()

        return now == cache_date

    def __init__(self) -> None:
        self.__theme = "dark"
        self.cache_filename = './cache/btc_daily.csv'
        self.btc_daily = pd.DataFrame()

    @property
    def theme(self) -> str:
        return self.__theme
    
    @theme.setter
    def theme(self, value: str) -> None:
        self.__theme = value

    def get_crypto_data(self) -> None:
        if (self._is_valid_cache()):
            self.btc_daily = pd.read_csv(self.cache_filename) 
            return None

        btc_curr = CryptoCurrencies(key=os.getenv("API_KEY"), output_format='pandas')
        btc_daily, _ = btc_curr.get_digital_currency_daily(symbol='BTC', market='USD')
        self.btc_daily = pd.DataFrame.from_dict(btc_daily);
    
        self._preprocessing()


    def _preprocessing(self) -> None:
        columns = ['1a. open (USD)', '2a. high (USD)', '3a. low (USD)', '4a. close (USD)', '5. volume']
        
        self.btc_daily.index = pd.to_datetime(self.btc_daily.index)
        self.btc_daily = self.btc_daily.T.drop_duplicates().T
        
        self.btc_daily.sort_index(inplace=True)

        for column in columns:
            self.btc_daily[column] = pd.to_numeric(self.btc_daily[column])

        self.__save_cache(self.btc_daily)