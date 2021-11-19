

.PHONY: up
up:
	docker compose -f docker/docker-compose.yml up

.PHONY: down
down:
	docker compose -f docker/docker-compose.yml down


.PHONY: build
build:
	. venv/bin/activate \
	&& python spampy/setup.py sdist bdist_wheel
