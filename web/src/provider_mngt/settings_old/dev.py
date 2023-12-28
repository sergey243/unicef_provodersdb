import os
from django.urls import reverse_lazy
from .base import *


try:
    from .local import *
except ImportError:
    pass
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

'''EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'admin <serge.testing243@gmail.com>' 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'serge.testing243@gmail.com' #hello@teamcfe.com
EMAIL_MAIN = 'serge.testing243@gmail.com'
EMAIL_HOST_PASSWORD = '243@mytest'
EMAIL_PORT = 587


ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = reverse_lazy('account_confirm_complete')
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = reverse_lazy('account_confirm_complete')'''