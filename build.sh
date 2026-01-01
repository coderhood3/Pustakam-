#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Force clean static collection
python manage.py collectstatic --noinput --clear

python manage.py migrate
