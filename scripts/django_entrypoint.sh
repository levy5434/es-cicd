#!/bin/bash
source .venv/bin/activate
cd src
python manage.py wait_for_db
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input
#python manage.py initialize_superuser
python manage.py runserver 0.0.0.0:8001
