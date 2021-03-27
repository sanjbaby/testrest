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

@app.route("/tasks")
def get_all_tasks():
    tasks = db.task.find()
    data = []
    for task in tasks:
        item = {
            "id": str(task["_id"]),
            "task": task["task"]
        }
        data.append(item)
    return jsonify(data=data)
    

if __name__ == '__main__':
    # Running app in debug mode
    app.run(debug=True,host='0.0.0.0',port=8080)
