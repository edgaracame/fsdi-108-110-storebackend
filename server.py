from flask import Flask, request
from about import me
from data import mock_data
import json
import random

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


@app.get("/api/products")
def products():
    return json.dumps(mock_data)


@app.post("/api/products")
def save_product():
    product = request.get_json()

    mock_data.append(product)
    product["id"] = str(random.randint(1, 123456789))

    return json.dumps(product)


@app.get("/api/products/<id>")
def get_product_by_id(id):
    for m in mock_data:
        if(m["id"] == str(id)):
            return json.dumps(m)
    return "Not Found"


@app.get("/api/products_category/<category>")
def get_products_by_category(category):
    results = []
    for m in mock_data:
        if(m["genre"].lower() == str(category).lower()):
            results.append(m)
    return json.dumps(results)


@app.get("/api/product_cheapest")
def get_cheapest():
    cheapest = mock_data[0]
    for m in mock_data:
        if(m["price"] < cheapest["price"]):
            cheapest = m
    return cheapest


@app.get("/api/categories")
def get_categories():
    genres = []
    for m in mock_data:
        if not m["genre"] in genres:
            genres.append(m["genre"])
    return json.dumps(genres)


@app.get("/api/count_products")
def get_products_count():
    count = len(mock_data)
    return json.dumps(f"There are {count} products in the catalog")


@app.get("/api/search/<text>")
def get_products_by_title(text):
    results = []
    for m in mock_data:
        if(text.lower() in m["title"].lower()):
            results.append(m)
    return json.dumps(results)


app.run(debug=True)
