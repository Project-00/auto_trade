import datetime
import numpy

"""
共通メソッドクラス
"""
class Util:
    """
    取引する時間帯か判定
    """
    @staticmethod
    def is_trading_time():
        jst = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
        hour = datetime.datetime.now(jst).hour
        return hour >= 7 & hour <= 24

    """
    市場が開いている曜日か判定
    """
    @staticmethod
    def is_market_open_date():
        weekday_index = datetime.date.today().weekday()
        return weekday_index >= 0 & weekday_index <= 4

    """
    差分の絶対値が設定値より広いか判定
    """
    @staticmethod
    def is_variation_wider(a, b, v):
        return numpy.abs(a - b) > numpy.abs(v)

    """
    差分の絶対値が設定値より狭いか判定
    """
    @staticmethod
    def is_variation_narrower(a, b, v):
        return numpy.abs(a - b) < numpy.abs(v)
