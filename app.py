from flask import Flask, jsonify, request
import sqlite3
app = Flask(__name__)

def get_db_connection():
    conn= sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    return conn

products = [
        {"id":1, "name": "Keyboard", "price":49.99},
        {"id":2, "name": "Mouse", "price":29.99}
    ]

@app.route("/")
def home():
    return jsonify({"message":"Hello from our first Flask Server!"})

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/products", methods =["POST"])
def add_products():
    data = request.get_json()
    new_product = {
        "id": len(products) + 1,
        "name": data.get("name"),
        "price":data.get("price")
    }
    products.append(new_product)
    return jsonify({"message": "Product added", "product": new_product}), 201
if __name__ =="__main__":
    app.run(debug=True)
