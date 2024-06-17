import os


base_dir = os.path.dirname(os.path.abspath(__file__))


host = os.getenv("FLASK_HOST", "0.0.0.0")
port = os.getenv("FLASK_PORT", 8080)

wsgi_app = "wsgi:vulnerablepython"
bind = f"{host}:{port}"
workers = 1
threads = 1
backlog = 2048
# daemon = True
loglevel = "info"
accesslog = os.path.join(base_dir, "access.log")
errorlog = os.path.join(base_dir, "gunicorn.log")
