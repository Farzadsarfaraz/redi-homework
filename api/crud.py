from flask import Flask, jsonify, request

# Create a Flask app
app = Flask(__name__)

users = [
    {"id": "1", "name": "Ali"},
    {"id": "2", "name": "mmm"}
]

products = []

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/product", methods=["POST"])
def add_product():
    data = request.get_json()
    
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Product must have name and price"}), 400

    existing = next((p for p in products if p["id"] == data["id"]), None)
    if existing:
        return jsonify({"error": "The product already exists"}), 400

    product = {
        "id": str(len(products) + 1),
        "name": data["name"],
        "price": data["price"]
    }
    products.append(product)
    return jsonify(product), 201

@app.route("/productGet", methods=["GET"])
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True)
