.PHONY: help clean

help: ## displays this help message.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)


clean: ## clean useless files
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.log' -exec rm -f {} +


prepare: ## create virtualenv and install requirements
	pdm install


prepare-db: ## create and initialize sqlite database
	sqlite3 instance/vulnerablepython.db ".read ./init.sql"


gunicorn-run:
	export FLASK_HOST=0.0.0.0 FLASK_PORT=8080
	pdm run gunicorn -c gunicorn.conf.py


run-dev:  ## run this application in development mode
	export ENV_TYPE=dev && pdm run wsgi.py


run-test:  ## run this application in test mode
	export ENV_TYPE=test && make gunicorn-run


run-prod:  ## run this application in production mode
	export ENV_TYPE=prod && make gunicorn-run

pack: clean ## pack the source code
	zip -r src.zip wsgi.py app
	mv src.zip ~/Desktop/