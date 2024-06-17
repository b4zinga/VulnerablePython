import logging
import os

from app import create_app


vulnerablepython = create_app(os.getenv("ENV_TYPE"))


if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    vulnerablepython.logger.handlers = gunicorn_logger.handlers
    vulnerablepython.logger.setLevel(gunicorn_logger.level)


if __name__ == "__main__":
    vulnerablepython.run()
