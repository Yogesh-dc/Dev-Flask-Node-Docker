from flask import Flask, jsonify
from flask_cors import CORS
from business import getdata

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Backend is running",
        "endpoints": ["/api"]
    })

@app.route('/api', methods=['GET'])
def api():
    data = getdata()
    data = {"data": data}
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0', debug=True)
