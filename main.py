from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route('/')
def all_data():
  return jsonify({
    'Data': data,
    'Message': 'Success'
  },
  200)


@app.route('/stars')
def star_data():
  name = request.args.get('name')
  stars_data = next(item for item in data if item[name] == name)
  return jsonify({
    'Data': data,
    'Message': 'Success'
  },
  200)

if (__name__ == '__main__'):
  app.run(debug = True)