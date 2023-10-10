# settings_dev.py

from .settings import *  # Import settings from the main settings file
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Development-specific settings
DEBUG = True

# Use SQLite for development (install 'sqlite3' if not already installed)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# A generic secret key for development
SECRET_KEY = 'django-insecure-*3$vgjb%i&+8h$e)8p708dvf06ex)u@lhhat#72&0_&kvk4j!y'
