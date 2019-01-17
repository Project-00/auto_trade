import pymongo
from src.model.db import Db

"""
予測値コレクションのDAOクラス
"""
class PUsdJpyRateDao(Db):

    def __init__(self):
        super(PUsdJpyRateDao, self).__init__()
        self._collection = 'P_USD_JPY_RATE'

    """
    売買判定用に最新の予測値ドキュメントを取得
    """
    def select_latest_doc(self):
        return self._db[self._collection].find_one(
            {}
            , {
                '_id': 0
                , 'open' : 1
                , 'close': 1
                , 'low' : 1
                , 'high': 1
            }
            , sort=[('time', pymongo.DESCENDING)]
        )
