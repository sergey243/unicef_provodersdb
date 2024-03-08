"""
Django settings for provider_mngt project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = Path(__file__).resolve().parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-yx%@%k82q")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (str(os.environ.get('DEBUG', '0') )== '1')

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS","*").split(" ")
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS","*").split(" ")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    'allauth',
    'allauth.account',
    'django_filters',
    'cities_light',
    'bootstrap5',
    'crispy_forms',
    "crispy_bootstrap5",
    'multiselectfield',
    'django_admin_listfilter_dropdown',
    "django_tables2",
    "bootstrap_datepicker_plus",
    'permissions_auditor',
    "profiles",
    'world',
    'providers',
    'dashboard',
    'utils',
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]
MIDDLEWARE = []
if DEBUG:
    # Debug configuration
    MIDDLEWARE +=  [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "allauth.account.middleware.AccountMiddleware",
        "django.middleware.locale.LocaleMiddleware",
        
    ]
else:
    # Production configuration
    MIDDLEWARE +=  [
        "django.middleware.security.SecurityMiddleware",
        'whitenoise.middleware.WhiteNoiseMiddleware',
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "allauth.account.middleware.AccountMiddleware",
        "django.middleware.locale.LocaleMiddleware",     
    ] 

ROOT_URLCONF = "provider_mngt.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [
            os.path.join(APP_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates'),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "provider_mngt.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DB = os.environ.get("POSTGRES_DB", None)
HOST = os.environ.get("DB_HOST", "localhost")
PORT = os.environ.get("DB_PORT", "5432")
USERNAME = os.environ.get("POSTGRES_USER", "user")
PASSWORD = os.environ.get("POSTGRES_PASSWORD", "password")
ENGINE = os.environ.get("ENGINE", None)

DATABASES = {
    "default": {
        "ENGINE": ENGINE,
        "NAME": DB,
        "USER": USERNAME,
        "PASSWORD": PASSWORD,
        "HOST": HOST,
        "PORT": PORT,
    }
}
if not DEBUG:
    #DATABASE_URL='postgres://{}:{}@{}:{}/{}?sslmode=require'.format(USERNAME,PASSWORD,HOST,PORT,DB)
    DATABASE_URL='postgres://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOST,PORT,DB)
    db_from_env = dj_database_url.config(default=DATABASE_URL,conn_max_age=500,engine=ENGINE)
    DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGES = [
    ('fr', _('French')),
    ('en', _('English')),
]

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

USE_L10N = True

LOCALE_PATHS = [
    os.path.join(APP_DIR, 'locale'),
]
PHRASE_ENABLED = True
PHRASE_PROJECT_ID = 'YOUR_PROJECT_ID'
PHRASE_PREFIX = '{{__'
PHRASE_SUFFIX = '__}}'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#STATIC_URL = "static/"
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(APP_DIR, 'static'),
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'public')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'tmp')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CITIES_LIGHT_TRANSLATION_LANGUAGES = ['fr', 'en']
CITIES_LIGHT_INCLUDE_COUNTRIES = ['CD']
CITIES_LIGHT_INCLUDE_CITY_TYPES = ['PPL', 'PPLA', 'PPLA2', 'PPLA3', 'PPLA4', 'PPLC', 'PPLF', 'PPLG', 'PPLL', 'PPLR', 'PPLS', 'STLMT',]



CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

DJANGO_TABLES2_TABLE_ATTRS = {
    'class': 'table table-hover',
}

LOGIN_REDIRECT_URL = '/'

# Whitenoise
STORAGES = {
    "staticfiles": {
        "BACKEND": 'django.contrib.staticfiles.storage.StaticFilesStorage'
    },
}


if not DEBUG:
    # Security settings for production
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True

# Allauth config
ACCOUNT_ADAPTER = 'profiles.adapter.MyAccountAdapter'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("DB_HOST", 'smtp.gmail.com')
EMAIL_PORT = os.environ.get("EMAIL_PORT",587)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
