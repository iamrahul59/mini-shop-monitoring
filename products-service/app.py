from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('products_requests_total', 'Total requests to products service')

products = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Phone", "price": 499},
    {"id": 3, "name": "Tablet", "price": 299}
]

@app.route('/products')
def get_products():
    REQUEST_COUNT.inc()
    return jsonify(products)

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
