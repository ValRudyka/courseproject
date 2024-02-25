from alpha_vantage.cryptocurrencies import CryptoCurrencies
import json
import datetime

class Model:
    def __load_cache(self) -> None | str:
        try:
            with open(self.cache_filename, 'r') as file:
                return json.load(file)
        except (IOError, json.JSONDecodeError):
            return None

    def __save_cache(self, data: dict) -> str:
        with open(self.cache_filename, 'w') as file:
            return json.dump(data, file)

    def clear_cache(self) -> None:
        with open(self.cache_filename, 'w'):
            pass

    def _is_valid_cache(self) -> bool:
        data = self.__load_cache()
        
        if (not data):
            return False

        cache_date = json.loads(data).get("date")
        
        cache_date = datetime.datetime.strptime(cache_date, '%d-%m-%y').date()
        now = datetime.datetime.now().date()

        return now == cache_date

    def __init__(self) -> None:
        self.__theme = "dark"
        self.cache_filename = './cache/btc_daily.json'
        self.btc_daily = {}

    @property
    def theme(self) -> str:
        return self.__theme
    
    @theme.setter
    def theme(self, value: str) -> None:
        self.__theme = value

    def get_crypto_data(self) -> None:
        if (self._is_valid_cache()):
            self.btc_daily = self.__load_cache()
            return None

        btc_curr = CryptoCurrencies(key='JT4JD9CMK0L9FOSG')
        btc_daily = btc_curr.get_digital_currency_daily(symbol='BTC', market='USD')
        self.btc_daily =  btc_daily 

        self.__save_cache(json.dumps({ "date" : datetime.datetime.now().date().strftime('%d-%m-%y'), "data": btc_daily }))

        