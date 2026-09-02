from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message":"Hello from our first Flask Server!"})

@app.route("/products", methods=["GET"])
def get_products():
    products = [
        {"id":1, "name": "Keyboard", "price":49.99},
        {"id":2, "name": "Mouse", "price":29.99}
    ]
    return jsonify(products)


if __name__ =="__main__":
    app.run(debug=True)
