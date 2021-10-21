PROJ_PATH = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))

cwd:
	cd $(PROJ_PATH)

build: cwd
	@if [ ! -f src/.env ]; then \
		echo "src/.env not found, check README.md for more info"; \
		exit 1; \
	fi
	docker build --tag=github_oauth .

rebuild: cwd
	docker build --no-cache --tag=github_oauth .

test: build
	docker run -it github_oauth python manage.py test -v 2

run: build
	docker run -p 8000:8000 github_oauth

shell: build
	docker run -it github_oauth python manage.py shell_plus
