from flask import Blueprint, request
from flask.json import jsonify
from project.users import controller


app = Blueprint('users', __name__)


@app.route('/users', methods=['GET'])
def users_get():
    users = controller.get_users()
    return jsonify({"data": users})


@app.route('/users/<user_id>', methods=['GET'])
def user_get(user_id):
    assert user_id == request.view_args['user_id']

    user = controller.get_user(user_id)
    if not user:
        return jsonify({"error": 'No user was found.'})

    return jsonify({"data": user})


@app.route('/users', methods=['POST'])
def users_post():
    new_user_data = request.json

    user = controller.insert_user(new_user_data)

    return jsonify({"data": user})


@app.route('/users/<user_id>', methods=['DELETE'])
def user_delete(user_id):
    assert user_id == request.view_args['user_id']

    user = controller.get_user(user_id)
    if not user:
        return jsonify({"error": 'No user was found.'})

    controller.delete_user(user)

    return jsonify({"data": 'User deleted successfully.'})


@app.route('/users/<user_id>', methods=['PATCH'])
def user_patch(user_id):
    assert user_id == request.view_args['user_id']
    user_update_data = request.json

    user = controller.get_user(user_id)
    if not user:
        return jsonify({"error": 'No user was found.'})

    updated_user = controller.update_user(user_id, user_update_data)

    return jsonify({"data": updated_user})
