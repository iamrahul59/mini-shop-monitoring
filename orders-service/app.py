from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('orders_requests_total', 'Total requests to orders service')

orders = [
    {"id": 1, "product": "Laptop", "quantity": 2},
    {"id": 2, "product": "Phone", "quantity": 1},
    {"id": 3, "product": "Tablet", "quantity": 3}
]

@app.route('/orders')
def get_orders():
    REQUEST_COUNT.inc()
    return jsonify(orders)

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
