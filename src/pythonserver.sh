#!/bin/bash
source virtualenvwrapper.sh
BASEDIR=$(dirname "$0")
cd $BASEDIR
workon djangodev
/usr/bin/firefox http://127.0.0.1:8000/
wait
python manage.py runserver
wait
