from .base import *
import os
from dotenv import load_dotenv 

load_dotenv() 


# Project settings
ALLOWED_HOSTS=['127.0.0.1','.sopranosomega.com']
DATABASE_URL = os.environ.get("DATABASE_URL", None)
DEBUG = False
DISABLE_COLLECTSTATIC = 1
SECRET_KEY=os.environ.get("SECRET_KEY", None)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("MYSQL_DATABASE"),
        'USER': os.environ.get("MYSQL_USERNAME"),
        'PASSWORD': os.environ.get("MYSQL_PASSWORD"),
        'HOST': 'localhost',
    }
}

STATIC_ROOT = BASE_DIR.parent / "static"