#!/usr/bin/env bash
set -e

export NO_DEBUG="1"

python manage.py migrate
python manage.py collectstatic --noinput

uwsgi --chdir=./ --ini=./uwsgi.ini