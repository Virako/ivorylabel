"""
Django settings for dashboard project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from os import environ as env


def env_list(env_name, default=list):
    """
    Get environment var and convert in python list. Example .env: APPS=x1,y2,z3
    """
    list_vars = env.get(env_name, None)
    return list_vars.split(',') if list_vars else default

def env_get_admins():
    """ Example: Foo:foo@test.com,Bar:bar@test.com """
    res = list()
    list_vars = env.get('ADMINS', '')
    admins = list_vars.split(',') if list_vars else list()
    for adm in admins:
        res.append(tuple(adm.split(':')))
    return tuple(res)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get('SECRET_KEY', 'example')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS: list[str] = env_list('ALLOWED_HOSTS', [])

ADMINS = env_get_admins()
MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ckeditor',
    'ckeditor_uploader',
    'contents',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dashboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db/db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = env.get('STATIC_URL', '/static2/static/')
STATIC_ROOT = env.get('STATIC_ROOT', None)
MEDIA_URL = env.get('MEDIA_URL', '/static2/media/')
MEDIA_ROOT = env.get('MEDIA_ROOT', None)


# Emails
SERVER_EMAIL = 'il@localhost'
DEFAULT_FROM_EMAIL = SERVER_EMAIL
EMAIL_HOST = env.get('EMAIL_HOST', 'email-smtp.eu-west-1.amazonaws.com')
EMAIL_PORT = int(env.get('EMAIL_PORT', 587))
EMAIL_HOST_USER = env.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = env.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = env.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_BACKEND = env.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')

# ckeditor
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_RESTRICT_BY_DATE = True
CKEDITOR_CONFIGS = {
    'default': {
        'height': 120,
        'width': 480,
    },
}
