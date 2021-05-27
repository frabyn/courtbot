HOST=127.0.0.1
TEST_PATH=./

# system python interpreter. used only to create virtual environment
PY = python3
VENV = venv
BIN=$(VENV)/bin

$(VENV): requirements.txt requirements-dev.txt
	$(PY) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install --upgrade wheel
	$(BIN)/pip install --upgrade -r requirements.txt
	$(BIN)/pip install --upgrade -r requirements-dev.txt
	touch $(VENV)

build: $(VENV)
	python manage.py makemigrations --noinput
	python manage.py migrate --noinput
	python manage.py collectstatic --noinput

lint: $(VENV)
	$(BIN)/flake8 . --exclude=venv --exclude=*.tox

run: $(VENV)
	python manage.py runserver

clean:
	rm -rf $(VENV)
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete
