from flask import Flask, request
from bson import ObjectId
from about import me
from data import mock_data
from config import db
import random
import json

app = Flask("server")


@app.get("/")
def home():
    return "Hello from flask server"


@app.get("/test")
def test():
    return "This is just a simple test"


@app.get("/about")
def about():
    return "Edgar Antonio Castillo Medina"

# API ENDPOINTS = PRODUCTS #


@app.get("/api/version")
def version():
    return "1.0"


@app.get("/api/about")
def about_json():
    return json.dumps(me)  # parse the dictionary into a json string


def fix_mongo_id(obj):
    obj["id"] = str(obj["_id"])
    del obj["_id"]
    return obj


@app.get("/api/products")
def products():
    cursor = db.products.find({})
    products = []
    for c in cursor:
        fix_mongo_id(c)
        products.append(c)

    return json.dumps(products)


@app.post("/api/products")
def save_product():
    product = request.get_json()

    db.products.insert_one(product)
    fix_mongo_id(product)

    return json.dumps(product)


@app.get("/api/products/<id>")
def get_product_by_id(id):
    product = db.products.find_one({"_id": ObjectId(id)})
    if not product:
        return "Not Found"

    fix_mongo_id(product)
    return json.dumps(product)


@app.get("/api/categories")
def get_categories():
    cursor = db.products.find({})
    genres = []
    for c in cursor:
        if not c["genre"] in genres:
            genres.append(c["genre"])

    return json.dumps(genres)


@app.get("/api/products_category/<category>")
def get_products_by_category(category):
    cursor = db.products.find({"genre": category})
    results = []
    for c in cursor:
        fix_mongo_id(c)
        results.append(c)

    return json.dumps(results)


@app.get("/api/product_cheapest")
def get_cheapest():
    cursor = db.products.find({})
    cheapest = cursor[0]
    for c in cursor:
        if(c["price"] < cheapest["price"]):
            cheapest = c

    fix_mongo_id(cheapest)
    return json.dumps(cheapest)


@app.get("/api/count_products")
def get_products_count():
    cursor = db.products.find({})
    count = 0
    for c in cursor:
        count += 1

    return json.dumps(f"There are {count} products in the catalog")


@app.get("/api/search/<text>")
def get_products_by_title(text):
    results = []
    for m in mock_data:
        if(text.lower() in m["title"].lower()):
            results.append(m)
    return json.dumps(results)


app.run(debug=True)
