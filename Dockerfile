FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \ 
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

# For Django
CMD ["python3", "manage.py", "makemigrations"]
CMD ["python3", "manage.py", "migrate"]
EXPOSE 8080
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
