from flask import Flask, jsonify, request, abort
from data_dummy import *

app = Flask(__name__)


@app.route('/parking_tool/api/v1.0/cars', methods=['POST'])
def add_car():
    if not request.json or not 'check_in' in request.json:
        abort(400)
    print(request.json)
    car = {
        'id': cars[-1]['id'] + 1,
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
    cars.append(car)
    return jsonify({'car': car}), 201


@app.route('/parking_tool/api/v1.0/cars', methods=['GET'])
def show_cars():
    return jsonify({'cars': cars})


"""
def drop_car():
    pass

def show_cars():
    pass
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
