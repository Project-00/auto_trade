from src.model.util import Util

"""
自動取引ロジッククラス
当日の予測値のみを用いる
"""
class OnlyLatestPDayLogic:
    def __init__(self, p_dict, _oanda):
        self.SELL = 'sell'
        self.BUY = 'buy'
        self.ASK = 'ask'
        self.BID = 'bid'
        self._o = p_dict['open']
        self._c = p_dict['close']
        self._h = p_dict['high']
        self._l = p_dict['low']
        self._v = 20 # TODO 設定ファイルから変更できるようにする
        self._v_yen = 0.01
        self._u = 10000
        self._oanda = _oanda

    """
    当日の予測値のみから売買の判定を行う

    """
    def get_trade_logic(self):
        # 設定値より予測の値段に幅がある場合のみ売買する
        if Util.is_variation_wider(self._o, self._c, self._v):
            # 始値＞終値
            if self._o > self._c:
                return self.short_trade
            else:
                # 終値＞始値
                return self.long_trade
        else:
            return None

    """
    
    """
    def is_able_trading(self):
        account = self._oanda.fetch_account_info()
        return account.get('balance') > self._u

    """
    終値＞始値の場合
    """
    def long_trade(self):
        if self.is_able_trading():
            current_rate = self._oanda.fetch_current_rate(self.ASK)

            # 始値で買い
            if Util.is_variation_narrower(current_rate, self._o, self._v_yen):
                self._oanda.create_order(self._u, self.BUY)

            # 安値で買い
            elif Util.is_variation_narrower(current_rate, self._l, self._v_yen):
                self._oanda.create_order(self._u, self.BUY)

            # 高値で全額決済
            elif Util.is_variation_narrower(current_rate, self._h, self._v_yen):
                self._oanda.close_positions()

            # 終値で全額決済
            elif Util.is_variation_narrower(current_rate, self._c, self._v_yen):
                self._oanda.close_positions()

    """
    始値＞終値の場合
    """
    def short_trade(self):
        if self.is_able_trading():
            current_rate = self._oanda.fetch_current_rate(self.ASK)

            # 始値で売り
            if Util.is_variation_narrower(current_rate, self._o, self._v_yen):
                self._oanda.create_order(self._u, self.SELL)

            # 高値で売り
            elif Util.is_variation_narrower(current_rate, self._l, self._v_yen):
                self._oanda.create_order(self._u, self.SELL)

            # 安値で全額決済
            elif Util.is_variation_narrower(current_rate, self._h, self._v_yen):
                self._oanda.close_positions()

            # 終値で全額決済
            elif Util.is_variation_narrower(current_rate, self._c, self._v_yen):
                self._oanda.close_positions()
