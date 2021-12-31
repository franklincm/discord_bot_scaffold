install: poetry.lock
	poetry install
	pre-commit install
	git config --bool flake8.strict true

requirements: poetry.lock
	install
	poetry export -f requirements.txt > requirements.txt

run: Dockerfile
	docker build -t scaffold .

stop: Dockerfile
	docker-compose down

build: setup.py
	python setup.py sdist bdist_wheel

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
