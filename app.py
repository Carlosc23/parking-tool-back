from flask import Flask, jsonify, request, abort
from bson import Binary, Code
from bson.json_util import dumps
import json
# from data_dummy import *
from connect import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/parking_tool/api/v1.0/send/cars', methods=['POST'])
def add_car():
    if not request.json or not 'check_in' in request.json:
        abort(400)
    print(request.json)
    id_1 = retrieve_id()
    car = {
              'id': id_1 + 1,
              'time': {
                  'check_in': request.json['check_in'],
                  'departure': request.json['departure']
              },
              'vehicle': {
                  'color': request.json['color'],
                  'brand': request.json['brand'],
                  'specialn': request.json['specialn'],
                  'type': request.json['type']
              },
              'position': request.json['position']
          },
    car2 = {
        'time': {
            'check_in': request.json['check_in'],
            'departure': request.json['departure']
        },
        'vehicle': {
            'color': request.json['color'],
            'brand': request.json['brand'],
            'specialn': request.json['specialn'],
            'type': request.json['type']
        },
        'position': request.json['position']
    }
    a = dict(car[0])
    add_car_hist(a)
    add_car_actual(car2)
    return "Ok"


@app.route('/parking_tool/api/v1.0/hist/cars', methods=['GET'])
def show_hist_cars():
    cars = list(retrieve_hist_cars())
    json_cars = json.loads(dumps(cars))
    print(json_cars)
    return jsonify({'cars': json_cars})


@app.route('/parking_tool/api/v1.0/actual/cars', methods=['GET'])
def show_actual_cars():
    cars = list(retrieve_actual_cars())
    json_cars = json.loads(dumps(cars))
    print(json_cars)
    return jsonify({'cars': json_cars})


@app.route('/parking_tool/api/v1.0/actual/drop/cars', methods=['POST'])
def empty_parking():
    position = request.json["position"]
    return drop_car(position)


"""

"""

"""
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})
"""
if __name__ == '__main__':
    app.run(debug=True)
