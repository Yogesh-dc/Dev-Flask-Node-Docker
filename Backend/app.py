from flask import Flask, jsonify, request
from flask_cors import CORS
from business import getdata, add_user

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Backend is running",
        "endpoints": ["/api", "/api/add"]
    })

@app.route('/api', methods=['GET'])
def api():
    data = getdata()
    return jsonify({"data": data})

@app.route('/api/add', methods=['POST'])
def add_user_route():
    payload = request.get_json(silent=True) or {}
    value = payload.get("value")
    if not value:
        return jsonify({"error": "Missing 'value' field"}), 400

    result = add_user(value)
    return jsonify(result), 201

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
