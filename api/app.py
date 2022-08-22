from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from pymongo import mongo_client

app = Flask(__name__)


mongo = PyMongo(app)

MONGO_URI = "mongodb://127.0.0.1:27017"
client = mongo_client.MongoClient(MONGO_URI)
DB_NAME = "restdb1"

db = client[DB_NAME]
collection = db["products"]
collection.insert_one({"name": "mouse", "price": 200})


@app.route("/", methods=["GET"])
def ping():
    return jsonify({"response": "Hello World!"})


@app.route("/api/new", methods=["POST"])
def new_product():
    new_item = request.get_json()
    collection.insert_one(new_item)
    return jsonify({"msg": "Added product successfully"}), 201


@app.route("/api/products", methods=["GET"])
def get_product():
    requested_item = request.get_json()
    requested_item_id = requested_item["id"]
    item_from_db = collection.find_one({"id": requested_item_id})
    if item_from_db:
        del item_from_db["_id"]
        return jsonify({"products": item_from_db}), 200
    else:
        return jsonify({"msg": "Product not found"}), 404


@app.route("/api/products/", methods=["DELETE"])
def delete_product():
    requested_item = request.get_json()
    requested_item_id = requested_item["id"]
    collection.delete_one({"id": requested_item_id})
    return jsonify({"msg": "Deleted product successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True)
