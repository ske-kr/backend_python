#!/bin/sh
poetry install
poetry shell
cd meronia
yes | python manage.py makemigrations --settings=meronia.settings
echo "==> Django setup, executing: migrate pro"
python manage.py migrate --settings=meronia.settings --fake-initial
echo "==> Django setup, executing: collectstatic"
python manage.py collectstatic --settings=meronia.settings --noinput -v 3
echo "==> Django deploy"
gunicorn -b 0.0.0.0:8000 --env DJANGO_SETTINGS_MODULE=meronia.settings meronia.wsgi:application
