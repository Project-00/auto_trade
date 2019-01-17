from src.model.dao.p_usd_jpy_rate_dao import PUsdJpyRateDao
from src.model.logic.only_latest_p_day_logic import OnlyLatestPDayLogic
from src.api.oanda import OandaWrapper

"""
自動取引サービスクラス
"""
class OnlyLatestPDayService:
    """
    当日の売買に使用するロジックを取得

    """
    @staticmethod
    def get_trade_logic():
        p_usd_jpy_rate_dao = PUsdJpyRateDao()
        p_dict = p_usd_jpy_rate_dao.select_latest_doc()

        _oanda = OandaWrapper()

        _logic = OnlyLatestPDayLogic(p_dict, _oanda)

        return  _logic.get_trade_logic()

    """
    保有ポジションを全額決済
    """
    @staticmethod
    def close_all_positions():
        _oanda = OandaWrapper()
        _oanda.close_positions()