import os
from .base import *

DEBUG = True

try:
    from .local import *
except ImportError:
    pass

#SECRET_KEY = '$gju)*ny#&ju4-7f(n!6a*$n48m%=u3=xw47*dcq^$gs6(zqo9'
#ALLOWED_HOSTS = ['134.209.184.220', '']

CSRF_TRUSTED_ORIGINS =  os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'admin <serge.testing243@gmail.com>' 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'serge.testing243@gmail.com' #hello@teamcfe.com
EMAIL_MAIN = 'serge.testing243@gmail.com'
EMAIL_HOST_PASSWORD = '243@mytest'
EMAIL_PORT = 587

