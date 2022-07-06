from flask import Flask
from about import me
from data import mock_data
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


@app.get("/api/products")
def products():
    return json.dumps(mock_data)


@app.get("/api/products/<id>")
def get_product_by_id(id):
    for m in mock_data:
        if(m["id"] == str(id)):
            return json.dumps(m)

    return "Not Found"


app.run(debug=True)
