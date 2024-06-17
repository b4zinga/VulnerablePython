from flask import Blueprint, current_app, request
from sqlalchemy import text

from app.extensions import db
from app.models import UserModel
from app.utils import response

sqli_bp = Blueprint("sqli", __name__)


# 存在漏洞
# 使用字符串拼接，存在SQL注入漏洞
# 传入 1?username=1'+select+*+from+user; 即可查询全量用户
@sqli_bp.get("/1")
def sqli1():
    username = request.args.get("username")
    sql = text(f"SELECT * FROM user WHERE username={username};")
    result = db.session.execute(sql)
    data = []
    for user in result.fetchall():
        data.append(user._asdict())
    return response.success(data)


# 修复漏洞
# 使用参数绑定修复SQL注入漏洞
@sqli_bp.get("/2")
def sqli2():
    username = request.args.get("username")
    sql = text("SELECT * FROM user WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    data = []
    for user in result:
        data.append(user._asdict())
    return response.success(data)


# 修复漏洞
# 使用ORM查询
@sqli_bp.get("/3")
def sqli3():
    try:
        username = request.args.get("username")
        user = (
            db.session.query(UserModel).filter(UserModel.username == username).first()
        )
        data = []
        if user:
            data = user.json()
        return response.success(data)
    except Exception as e:
        current_app.logger.error(f"query user error, {e}")
        return response.failed()
