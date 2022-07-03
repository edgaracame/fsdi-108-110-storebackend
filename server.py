from flask import Flask

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


app.run(debug=True)
