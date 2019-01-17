from src.config import Config
from oandapy import API
from oandapy.exceptions import OandaError # TODO try-cacthで書く

"""
oandapyのラッパークラス
"""
class OandaWrapper:
    def __init__(self):
        self.MARKET = 'market'
        self.STOP = 'stop'
        self.LIMIT = 'limit'
        self.USD_JPY = 'USD_JPY'

        _oanda_section = Config.get_oanda_section()

        self._account_id = int(_oanda_section['ACCOUNT_ID'])
        self._oanda = API(environment='practice', access_token=_oanda_section['API_KEY'])

    """
    アカウント情報の取得
    """
    def fetch_account_info(self):
        return self._oanda.get_account(account_id=self._account_id)

    """
    現在のレートを取得
    """
    def fetch_current_rate(self):
        res = self._oanda.get_prices(instruments=self.USD_JPY)
        return res.get('prices')[0]

    """
    現在の保有ポジションを取得
    """
    def fetch_positions(self):
        return self._oanda.get_positions(account_id=self._account_id)

    """
    現在の未約定新規注文を取得
    """
    def fetch_open_orders(self):
        return self._oanda.get_orders(account_id=self._account_id)

    """
    取引履歴を取得
    """
    def fetch_transaction_history(self):
        return self._oanda.get_transaction_history(account_id=self._account_id)

    """
    注文(新規,決済)
    現在保有するポジションと逆の注文を入れることで決済される
    """
    def create_order(self, units, side):
        return self._oanda.create_order(
            account_id= self._account_id
            , instrument = self.USD_JPY
            , units = units
            , side = side
            , type = self.MARKET
        )

    """
    現在保有しているポジションを全て決済
    """
    def close_positions(self):
        return self._oanda.close_position(
            account_id=self._account_id
            , instrument=self.USD_JPY
        )
