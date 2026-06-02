run:
	python src/main.py

test:
	python -m pytest tests/

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
