from flask import Flask, request, jsonify
from flask_cors import CORS
from business import getdata

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET'])
def api():
    data = getdata()
    data = {"data": data}
    return jsonify(data)

if __name__ == '__main__':
    app.run()
