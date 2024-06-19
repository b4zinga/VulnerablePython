from flask import Blueprint, request

from app.utils import response


xss_bp = Blueprint("xss", __name__)


@xss_bp.get("/1")
def xss1():
    msg = request.args.get("msg")
    return msg


@xss_bp.get("/2")
def xss2():
    msg = request.args.get("msg")
    return response.success(msg)
