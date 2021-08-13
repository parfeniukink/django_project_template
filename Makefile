PYTHON = python3

# Django
DJANGO_DEBUG_HOST = 0.0.0.0
DJANGO_DEBUG_PORT = 8000
DJANGO_RUNSERVER_COMMAND = ${PYTHON} src/manage.py runserver ${DJANGO_DEBUG_HOST}:${DJANGO_DEBUG_PORT}

# Linter
FLAKE8_BASE_COMMAND = flake8
PYTEST_BASE_COMMAND = pytest

# Formatters
BLACK_BASE_COMMAND = black
ISORT_BASE_COMMAND = isort


.PHONY: django-server
django-server:
	${DJANGO_RUNSERVER_COMMAND}

.PHONY: run-tests
run-tests:
	cd src && ${PYTEST_BASE_COMMAND}


.PHONY: check-lint
check-lint:
	${FLAKE8_BASE_COMMAND} .

.PHONY: fix-codestyle
fix-codestyle:
	${BLACK_BASE_COMMAND} . && ${ISORT_BASE_COMMAND} .
