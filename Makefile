run:
	python src/main.py

docker-build:
	docker build -t momentum-strategy .

docker-run:
	docker run --rm momentum-strategy

docker-compose-up:
	docker compose up
