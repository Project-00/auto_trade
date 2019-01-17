from pymongo import MongoClient
from src.config import Config

"""
DB接続クラス
"""
class Db:
    """
    DB接続
    """
    def __init__(self):
        _dbs = Config.get_db_section()
        _client = MongoClient(_dbs['IP_ADDRESS'], int(_dbs['PORT']))
        _client.admin.authenticate(_dbs['ID'], _dbs['PASS'])
        self._db = _client.AUTO_TRADE_DB

