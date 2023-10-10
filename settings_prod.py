# settings_prod.py

from .settings import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Update DEBUG setting for production
DEBUG = False

# Add your production database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Add your production secret key
SECRET_KEY = 'e242a579f0002a8a1c32f96368a40021cc599def76aabf5298025618b67b7255b842f00ef9c3e5d09b5ad8e5075a9b8a2fae'
