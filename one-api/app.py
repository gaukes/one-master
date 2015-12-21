#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

# might want to replace with a database
# if empty, return all ids
# these ids are not recycled. if a user who had an id is deleted, that id will never be used again
next_id = 3

data = [
        {
                "id": 1,
                "name": u"Tom Cruise",
                "points": 100
        },
        {
                "id": 2,
                "name": u"Leonardo DiCaprio",
                "points": 0
        }
]


def get_points(ids):
        if len(ids) == 0:
                return data
        acceptable_ids = set(ids)
        output = []
        for d in data:
                if d['id'] in acceptable_ids:
                        output.append(d)
        return output

def add_points(user_id, points):
        for d in data:
                if d['id'] == user_id:
                        d['points'] += points
                        return d
        # this id doesn't exist
        return None

def add_user(user_id, name, points):
        global data
        new_data = {
                "id": user_id,
                "name": name,
                "points": points
        }
        data.append(new_data)
        return new_data

def del_users(user_ids):
        global data
        all_ids = [d['id'] for d in data]
        for u in user_ids:
                if u not in all_ids:
                        return False
        acceptable_ids = set(user_ids)
        new_data = []
        for d in data:
                if d['id'] not in acceptable_ids:
                        new_data.append(d)
        data = new_data
        return True


@app.route('/')
def index():
        return "Hello, World"

@app.route('/one/api/v1.0/points', methods=['GET'])
def api_get_points_users():
        return jsonify({'users': get_points([])})

@app.route('/one/api/v1.0/points/<int:user_id>', methods=['GET'])
def api_get_points_user(user_id):
        user_info = get_points([user_id])
        if len(user_info) == 0:
                abort(404)
        return jsonify({'users': user_info})

@app.route('/one/api/v1.0/points', methods=['POST'])
def api_add_user():
        global next_id
        if not request.json or not 'name' in request.json:
                abort(400)
        user = add_user(next_id, request.json['name'], 0)
        next_id += 1
        return jsonify({'users': user}), 201

@app.route('/one/api/v1.0/points/<int:user_id>', methods=['PUT'])
def update_user(user_id):
        if not request.json:
                abort(400)
        if 'points' not in request.json:
                abort(400)
        user = add_points(user_id, request.json['points'])
        if user == None:
                abort(400)
        return jsonify({'users': user})

@app.route('/one/api/v1.0/points/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
        result = del_users([user_id])
        if result == False:
                abort(400)
        return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify({'error': 'Not Found'}), 404)

@app.errorhandler(400)
def invalid_arguments(error):
        return make_response(jsonify({'error': 'Invalid Arguments'}), 400)

if __name__ == '__main__':
        app.run(debug=True)

