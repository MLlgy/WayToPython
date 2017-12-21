from flask import Flask, jsonify
from .lesson34_mysql import *

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world flask!!'


@app.route('/aline/api/v1.0/all', methods=['GET'])
def get_all():
    return jsonify({'data': query_table(), 'code': 200})


if __name__ == '__main__':
    app.run(debug=True)
