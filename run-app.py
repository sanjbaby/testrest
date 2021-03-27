# -*- coding: utf-8 -*-

from app import app
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import socket

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/sampledb"
mongo = PyMongo(app)
db = mongo.db

@app.route("/")
def index():
    hostname = socket.gethostname()
    return jsonify(
        message="Welcome to Tasks app! I am running inside {} pod!".format(hostname)
    )

if __name__ == '__main__':
    # Running app in debug mode
    app.run(debug=True,host='0.0.0.0',port=8080)