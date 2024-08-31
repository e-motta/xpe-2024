from pymongo import MongoClient

from .config import MONGODB_URI


class MongoDB:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client.get_database()
