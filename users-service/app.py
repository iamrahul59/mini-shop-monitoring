from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('users_requests_total', 'Total requests to users service')

users = [
    {"id": 1, "name": "Rahul", "email": "rahul@test.com"},
    {"id": 2, "name": "Bishal", "email": "bishal@test.com"},
    {"id": 3, "name": "John", "email": "john@test.com"}
]

@app.route('/users')
def get_users():
    REQUEST_COUNT.inc()
    return jsonify(users)

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
