from .base import *

ALLOWED_HOSTS = ['15.165.115.183', 'fdxtesting.kro.kr']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mysite',
        'USER': 'mysiteuser',
        'PASSWORD': '123123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}