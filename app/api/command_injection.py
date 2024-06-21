import os
from flask import Blueprint, request

from app.utils import response


cmd_bp = Blueprint("command_injection", __name__)


# 存在漏洞
# poc:
# /1?cmd=www.baidu.com;whoami
@cmd_bp.get("/1")
def command1():
    cmd = request.args.get("cmd")
    result = os.system(f"nslookup {cmd}")
    return response.success(result)
