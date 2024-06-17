from flask import Blueprint, jsonify


index_bp = Blueprint("index", __name__)


@index_bp.get("/")
def index():
    return "VulnerablePython"


@index_bp.get("/ping")
def ping():
    return jsonify({"msg": "pong"})
