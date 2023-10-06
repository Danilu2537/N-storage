from pathlib import Path

from envparse import env

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR.joinpath('.env')
if ENV_PATH.is_file():
    env.read_envfile(ENV_PATH)

SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = ['*']

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
DRF_APPS = ['rest_framework', 'drf_spectacular']
LOCAL_APPS = ['storages', 'movement']

INSTALLED_APPS = DJANGO_APPS + DRF_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nstorage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['reports/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }
]

REST_FRAMEWORK = {'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'}

SPECTACULAR_SETTINGS = {
    'TITLE': 'N-storage',
    'DESCRIPTION': 'n-storage',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

WSGI_APPLICATION = 'nstorage.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST', default='127.0.0.1'),
        'PORT': env.str('POSTGRES_PORT', default='5432'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.UserAttributeSimilarityValidator'
    },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR.joinpath('static')

STATICFILES_DIRS = ((BASE_DIR.joinpath('reports/static/')),)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
