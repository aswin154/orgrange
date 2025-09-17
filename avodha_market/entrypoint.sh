#!/bin/sh

echo "Applying database migrations..."
python manage.py migrate

echo "Starting server..."
exec gunicorn --bind 0.0.0.0:8000 --workers 3 avodha_market.wsgi:application
