from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app, resources={r"/login": {"origins": "*"}})

@app.route("/", methods=["GET"])
def holloWorld():
  return jsonify({"msg": "test orogin home"})

@app.route("/get", methods=["GET"])
def helloWorld():
  return jsonify({"msg": "test orogin"})

@app.route("/login", methods=["POST"])
@cross_origin()
def helloWorld2():
  return jsonify({"msg": "test allow cross orogin"})

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")