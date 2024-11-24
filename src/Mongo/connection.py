import os
from pymongo import MongoClient

DATABASE_NAME = "THDC"

__LOCALHOST_MONGO = "mongodb://localhost/THDC"

connection_string = os.getenv("MONGO_URL", __LOCALHOST_MONGO)

client = MongoClient(connection_string)
