from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({"status": "ok"})
