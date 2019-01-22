from src.api.oanda import OandaWrapper
from src.model.dao.p_usd_jpy_rate_dao import PUsdJpyRateDao
from src.model.logic.only_latest_p_close_logic import OnlyLatestPCloseLogic

"""
自動取引サービスクラス
"""
class OnlyLatestPCloseService:
    """
    当日の売買に使用するロジックを取得

    """
    @staticmethod
    def get_trade_logic():
        p_usd_jpy_rate_dao = PUsdJpyRateDao()
        p_dict = p_usd_jpy_rate_dao.select_latest_doc()

        _oanda = OandaWrapper()

        _logic = OnlyLatestPCloseLogic(p_dict, _oanda)

        return  _logic.get_trade_logic()

    # TODO 共通化
    """
    保有ポジションを全額決済
    """
    @staticmethod
    def close_all_positions():
        _oanda = OandaWrapper()
        return _oanda.close_positions()
