from flask import Flask, jsonify, Response
from redis import Redis
from configs import settings


app = Flask(__name__)
redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)


@app.route('/ping')
def ping() -> Response:
    return jsonify({"status": "ok"})


@app.route('/count')
def count() -> Response:
    redis.incr('visit_count')
    visit_count = redis.get('visit_count')
    return jsonify({'visit_count': int(visit_count.decode('utf-8'))})
