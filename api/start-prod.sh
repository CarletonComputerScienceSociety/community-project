#!/bin/bash

export DJANGO_SETTINGS_MODULE=api.settings.prod
gunicorn \
    -w 2 \
    -b 0.0.0.0:8000 \
    api.wsgi:application
