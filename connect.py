import pymongo
from db_credentials import *

connection = pymongo.MongoClient(HOST)
db = connection[NAME]
parking_lot_actual = db[COLLECTION_1]
parking_lot_historical = db[COLLECTION_2]


def add_car(car):
    parking_lot_actual.insert_one(car)
    parking_lot_historical.insert_one(car)


def show_cars():
    result = parking_lot_actual.find()
    cars_list = []
    for doc in result:
        cars_list.append(doc)


def retrieve_id():
    id_1 = parking_lot_actual.find()
    id_2 = parking_lot_historical.find()
    return id_1, id_2


"""add_car({
    'id': 1,
    'time': {
        'check_in': '3:30',
        'departure': '3:45'
    },
    'vehicle': {
        'color': 'blue',
        'brand': 'mazda',
        'specialn': False,
        'type': 'moto'
    },
    'position': ''
})
"""