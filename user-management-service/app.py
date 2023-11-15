# app.py
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_cors import CORS, cross_origin
from aws_controller import DynamodbTable

import boto3

app = Flask(__name__)
CORS(app, support_credentials=True)

table = DynamodbTable('anemone-user')



@app.route('/register', methods=['POST'])
@cross_origin(supports_credentials=True)
def register():

    data = request.get_json()

    email = data['email']

    # Check if user already exists
    if table.check_user_exist(email):
        return jsonify({'message': 'Email already exists'}), 400
    
    hashed_password = generate_password_hash(data['password'])

    table.add_user(email, hashed_password)

    return jsonify({'message': 'User created successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password_hash = table.get_password_hash(email)

    if table.check_user_exist(email) and check_password_hash(password_hash, data['password']):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401




if __name__ == '__main__':
    app.run()
