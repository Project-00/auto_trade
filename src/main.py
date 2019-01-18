import schedule
import time
from src.model.util import Util
from src.model.service.only_latest_p_day_service import OnlyLatestPDayService

# TODO ログ出力する
if __name__ == '__main__':
    # 土日を除く、07:00-24:00で取引
    if Util.is_market_open_date():
        logic = OnlyLatestPDayService.get_trade_logic()

        if logic is not None:
            schedule.every(1).minutes.do(logic)

            while True:
                if Util.is_trading_time():
                    schedule.run_pending()
                    time.sleep(1)
                else:
                    break

            # 念の為、当日分のポジションを手仕舞い
            OnlyLatestPDayService.close_all_positions()