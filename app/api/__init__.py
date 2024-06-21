from flask import Flask

from .index import index_bp
from .sql_injection import sqli_bp
from .ssrf import ssrf_bp
from .path_traversal import path_bp
from .code_injection import code_bp
from .command_injection import cmd_bp
from .xss import xss_bp


default_blueprints = [
    (index_bp, "/"),
    (sqli_bp, "/sqli"),
    (ssrf_bp, "/ssrf"),
    (path_bp, "/path"),
    (code_bp, "/code"),
    (cmd_bp, "/cmd"),
    (xss_bp, "/xss"),
]


def register_blueprints(app: Flask):
    for bp, prefix in default_blueprints:
        app.register_blueprint(bp, url_prefix=prefix)
