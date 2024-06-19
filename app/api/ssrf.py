from flask import Blueprint, request
import requests

from app.utils import response


ssrf_bp = Blueprint("ssrf", __name__)


# 存在漏洞
# 未经校验即向接收到的URL发送HTTP请求
# 传入 1?url=https://www.baidu.com/ 即可利用漏洞向baidu.com发送请求，获取回显
@ssrf_bp.get("/1")
def ssrf1():
    url = request.args.get("url")
    req = requests.get(url)
    return response.success(req.text)
