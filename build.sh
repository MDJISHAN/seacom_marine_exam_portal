#!/usr/bin/env bash

# Step 1: Install Python dependencies
pip install -r requirements.txt

# Step 2: Run database migrations
python manage.py migrate

# Step 3: Create superuser if it doesn't exist
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
import os

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if username and email and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"✅ Superuser {username} created.")
    else:
        print(f"ℹ️ Superuser {username} already exists.")
else:
    print("❌ Superuser environment variables not found.")
EOF
