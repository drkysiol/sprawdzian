from flask import Flask, jsonify, request
from .services import create_user, get_user, update_user, delete_user

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    users = [user.__dict__ for user in get_user(None)]
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(user.__dict__)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user_endpoint():
    data = request.get_json()
    user = create_user(data['firstName'], data['lastName'], data['birthYear'], data['group'])
    return jsonify(user.__dict__), 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user_endpoint(user_id):
    data = request.get_json()
    user = update_user(user_id, data.get('firstName'), data.get('lastName'), data.get('birthYear'), data.get('group'))
    if user:
        return jsonify(user.__dict__)
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_endpoint(user_id):
    delete_user(user_id)
    return jsonify({"message": "User deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)
