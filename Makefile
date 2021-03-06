.PHONY: default install dependency-prod dependency-develop dependency-update lint lint-ci package-check test test-html

# Run install-dep-develop job by default
default: dependency-develop

# Create a job that deploys this application to the system
install:
	python3 -m pip install --ignore-installed -U --compile -r requirements.txt .

install-pipenv:
	pipenv run pip install -e .

# Create a job to install dependencies needed for production
dependency-prod:
	pipenv sync

# Create a job to install dependencies needed for development
dependency-develop:
	pipenv install --dev --skip-lock

dependency-update:
	pipenv update
	jq -r '.default | to_entries[] | .key + .value.version' Pipfile.lock > requirements.txt

# Create a job for running pytlint on the src
lint:
	 pipenv run pylint ./src

# Create a modified job for CI for lint
lint-ci:
	 pipenv run pylint --exit-zero ./src

# Create a job to check for vulnerable packages installed
package-check:
	pipenv check

# Create a job for running tests on src folder and print coverage to cli
test:
	PYTHONPATH=./src pipenv run pytest tests --doctest-modules --cov=lazyboost

# Create a job to run pytest on src folder and generate coverage into xml and html
test-html:
	PYTHONPATH=./src pipenv run pytest tests --doctest-modules --junitxml=junit/test-results.xml \
	    --cov=lazyboost --cov-report=xml --cov-report=html
