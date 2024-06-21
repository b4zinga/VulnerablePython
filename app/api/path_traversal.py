from flask import Blueprint, request

from app.utils import response


path_bp = Blueprint("path_traversal", __name__)


# 存在漏洞
# poc:
# /1?path=/etc/passwd
@path_bp.get("/1")
def path1():
    p = request.args.get("path")
    with open(p, "r") as file:
        return response.success(file.read())


@path_bp.post("/2")
def path2():
    file = request.files["file"]
    file.save(file.filename)
    return response.success(file.filename)
