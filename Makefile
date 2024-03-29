setup:
	asdf install
	poetry install

fmt:
	poetry run black .
	poetry run isort .

test:
	poetry run pytest .

clean:
	rm -rf dist

build:
	poetry build

publish: clean build
	poetry publish

release: clean build
	ghr -u crflynn -r sqlalchemy-databricks -c $(shell git rev-parse HEAD) -delete -b "release" -n $(shell poetry version -s) $(shell poetry version -s) dist