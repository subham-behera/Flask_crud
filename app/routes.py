# routes.py

from flask import Blueprint, jsonify, request
from app.db import db

api_op = Blueprint('api', __name__)

@api_op.route('/data', methods=['GET'])
def get_json_data():
    cursor = db.get_cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    cursor.close()

    formatted_data = []
    for row in data:
        formatted_row = {
            'user_id': row[0],
            'name': row[1],
            'email': row[2],
            'phone_number': row[3],
            'location': row[4]
        }
        formatted_data.append(formatted_row)

    return jsonify(formatted_data)


@api_op.route('/data', methods=['POST'])
def add_data():
    new_data = request.get_json()
    cursor = db.get_cursor()
    sql = "INSERT INTO users (name, email, phone_number, location) VALUES (%s,%s,%s,%s);"
    cursor.execute(sql, (new_data['name'], new_data['email'], new_data['phone_number'], new_data['location']))
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Data added successfully"}), 201

@api_op.route('/data/<int:user_id>', methods=['DELETE'])
def delete_data(user_id):
    cursor = db.get_cursor()
    sql = "DELETE FROM users WHERE user_id = %s"
    cursor.execute(sql, (user_id,))
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Data deleted successfully"}), 200

@api_op.route('/data/<int:user_id>', methods=['PUT'])
def update_data(user_id):
    updated_data = request.get_json()
    cursor = db.get_cursor()
    sql = "UPDATE users SET name=%s, email=%s, phone_number=%s, location=%s WHERE user_id=%s"
    cursor.execute(sql, (updated_data['name'], updated_data['email'], updated_data['phone_number'], updated_data['location'], user_id))
    db.connection.commit()
    cursor.close()
    return jsonify({"message": "Data updated successfully"}), 200
