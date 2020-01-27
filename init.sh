#!/bin/bash

# Create and activate the virtualenv
rm -rf venv
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run migrations
cd pyfolio
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver
