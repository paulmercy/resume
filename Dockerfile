FROM python:3.9-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/

# CMD python manage.py runserver 0.0.0.0:8000

# CMD gunicorn resume.wsgi:application --bind 0.0.0.0:8000

CMD gunicorn -c conf/gunicorn_config.py resume.wsgi