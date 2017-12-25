from flask import Flask, jsonify
from lesson34_mysql import *

from LearnWithVideo.lesson34_mysql import *

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world flask!!'


@app.route('/aline/api/v1.0/all', methods=['GET'])
def get_all():
    return jsonify({'data': query_table(), 'code': 200})

@app.route('/aline/api/v1.0/all/<int:develop_id>',methods=['GET'])
def get_develop(develop_id):
    result = query_table(develop_id)
    return jsonify({'date':result})

@app.route('/aline/api/v1.0/delete',methods=['DELETE'])
def delete_table_url():
    result = delete_table()
    print(result)
    return jsonify({'code':200})


if __name__ == '__main__':
    app.run(port=1024,debug=True)
