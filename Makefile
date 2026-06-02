run:
	python src/main.py

test:
	python -m pytest tests/

sphinx-build:
	python -m sphinx.cmd.build -b html docs docs/_build/html

docker-test:
	docker run --rm teafox56a/tsmom-framework:latest python -m pytest -v tests/

render-local:
	quarto render report/report.qmd

docker-build:
	docker build -t teafox56a/tsmom-framework:latest .

docker-run:
	docker run --rm -v "$(CURRENT_DIR)/output:/app/output" teafox56a/tsmom-framework:latest

docker-compose-up:
	docker compose up

docker-push:
	docker push teafox56a/tsmom-framework:latest
