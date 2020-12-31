from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
import json

BASE_DIR = Path(__file__).resolve().parent.parent

with open("secret_key.json", "r", encoding="UTF-8") as f:
    secret_key = json.loads(f.read())

def get_secret_key(key, secret_key_list=secret_key):
    try:
        return secret_key_list[key]
    except KeyError:
        raise ImproperlyConfigured("{} 오류".format(key))


SECRET_KEY = get_secret_key("secret_key_django")

DEBUG = True

ALLOWED_HOSTS = ["*"]



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'main',
]

INTERNAL_IPS = ('127.0.0.1')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
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

WSGI_APPLICATION = 'conf.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':     get_secret_key("secret_database_key_name"),
        "USER":     get_secret_key("secret_database_key_user"),
        "PASSWORD": get_secret_key("secret_database_key_pw"),
        "HOST":     get_secret_key("secret_database_key_host"),
        "PORT":     get_secret_key("secret_database_key_port"),
    }
}

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



LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media' 