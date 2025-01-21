from .base import *


# Project settings
ALLOWED_HOSTS=['.sopranosomega.com']
DATABASE_URL = os.environ.get("DATABASE_URL", None)
DEBUG = False
DISABLE_COLLECTSTATIC = 1
SECRET_KEY=os.environ.get("SECRET_KEY", None)
