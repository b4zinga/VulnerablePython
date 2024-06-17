from flask import Flask

from .index import index_bp
from .sql_injection import sqli_bp
from .ssrf import ssrf_bp


default_blueprints = [
    (index_bp, "/"),
    (sqli_bp, "/sqli"),
    (ssrf_bp, "/ssrf"),
]


def register_blueprints(app: Flask):
    for bp, prefix in default_blueprints:
        app.register_blueprint(bp, url_prefix=prefix)
