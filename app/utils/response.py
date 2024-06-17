from flask import Response, jsonify


def success(data=None, msg: str = "success", code: int = 200, **kwargs) -> Response:
    """
    return success json response
    """
    result = {"code": code, "data": data, "msg": msg, **kwargs}
    return jsonify(result)


def failed(msg: str = "failed", code: int = -1, data=None, **kwargs) -> Response:
    """
    return failed json response
    """
    result = {"code": code, "data": data, "msg": msg, **kwargs}
    return jsonify(result)
