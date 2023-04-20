from flask import Flask, request, jsonify
from redis import Redis
import json

app = Flask(__name__)
redis = Redis(host="redis", db=0, socket_timeout=5, charset="utf-8")

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        data = request.get_json()
        name = data['name']
        redis.rpush('students', name)
        return jsonify({'name': name})
    
    if request.method == 'GET':
        students = redis.lrange('students', 0, -1)
        return jsonify(students[0].decode())