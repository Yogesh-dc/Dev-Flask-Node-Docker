from flask import Flask, request, jsonify
from business import getdata
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/api', methods=['GET'])
def api():
    data = getdata()
    data = {"data": data}
    return jsonify(data)

if __name__ == '__main__':
    app.run()
