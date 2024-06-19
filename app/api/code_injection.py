from flask import Blueprint, request

from app.utils import response


code_bp = Blueprint("code_injection", __name__)


@code_bp.get("/1")
def code1():
    s = request.args.get("code")
    result = eval(s)
    return response.success(result)
