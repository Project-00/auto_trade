"""
自動取引ロジッククラス
当日の予測終値のみを用いる
"""
class OnlyLatestPCloseLogic:
    def __init__(self, p_dict, _oanda):
        self.SELL = 'sell'
        self.BUY = 'buy'
        self.ASK = 'ask'
        self.BID = 'bid'
        self._c = p_dict['close']
        self._v_yen = 0.1 # TODO 設定ファイルから変更できるようにする
        self._u = 10000
        self._oanda = _oanda

        print('本日の予測終値は%sです' % self._c)# TODO ログ出力する

    """
    売買ロジックの取得
    """
    def get_trade_logic(self):
        return self.trade_logic

    """
    売買ロジック
    予測終値からxpips以上乖離があれば注文
    """
    def trade_logic(self):
        if self.is_able_trading():
            current_rate = self._oanda.fetch_current_rate()

            if self.is_higher_than_close(current_rate):
                print(self._oanda.create_order(self._u, self.SELL))# TODO ログ出力する

            elif self.is_lower_than_close(current_rate):
                print(self._oanda.create_order(self._u, self.BUY))# TODO ログ出力する

            else:
                print('取引が行われませんでした')# TODO ログ出力する

    """
    売買できる残高があるか判定
    """
    def is_able_trading(self):
        account = self._oanda.fetch_account_info()
        return account.get('balance') > self._u

    """
    現在の値が、予測終値よりxpips以上高いか判定
    """
    def is_higher_than_close(self, current_rate):
        return current_rate[self.BID] - self._c  > self._v_yen

    """
    現在の値が、予測終値よりxpips以上低いか判定
    """
    def is_lower_than_close(self, current_rate):
        return  self._c - current_rate[self.ASK] > self._v_yen
