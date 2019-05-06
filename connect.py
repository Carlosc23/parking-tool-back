import pymongo
from db_credentials import *

connection = pymongo.MongoClient(HOST)
db = connection[NAME]
parking_lot_actual = db[COLLECTION_1]
parking_lot_historical = db[COLLECTION_2]


def add_car_actual(car):
    parking_lot_actual.insert_one(car)


def add_car_hist(car):
    parking_lot_historical.insert_one(car)


def retrieve_hist_cars():
    result = parking_lot_historical.find()
    cars_list = []
    for doc in result:
        cars_list.append(doc)
    return cars_list


def retrieve_actual_cars():
    result = parking_lot_actual.find()
    cars_list = []
    for doc in result:
        cars_list.append(doc)
    return cars_list


def retrieve_id():
    result = parking_lot_historical.find()
    id_1 = result.count()
    print(id_1)
    return int(id_1)


def drop_car(position):
    query = {"position": position}
    parking_lot_actual.delete_one(query)
    return "Se ha vaciado el parqueo de la posicion: " + position


def set_departure_car(position, departure):
    filter, update = {"position": position}, {"$set": {"time.departure": departure}}
    parking_lot_actual.update_one(filter, update)
    car = parking_lot_actual.find_one(filter)
    add_car_hist(car)
    drop_car(position)


# print(retrieve_actual_cars()[1])
# print(retrieve_hist_cars())
# set_departure("B25","2:17")
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
