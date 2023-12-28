#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Adding super user
echo "Creating admin user"
python manage.py initadmin

# Start server
echo "Starting server"
#python manage.py runserver 0.0.0.0:8000
