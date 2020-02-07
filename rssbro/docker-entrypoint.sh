#!/bin/sh
echo "Apply migrations"
python manage.py migrate

echo "Fetch current exchange"
python manage.py fetch
