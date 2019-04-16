import pymongo
from db_credentials import *

connection = pymongo.MongoClient(HOST)
db = connection[NAME]
parking_lot_actual = db[COLLECTION_1]
parking_lot_historical = db[COLLECTION_2]


def add_car():
    pass


def show_cars():
    pass
