#!/bin/sh

sleep 10

cd /apps/backend

. .venv/bin/activate

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn core.wsgi:application --bind 0.0.0.0:8000