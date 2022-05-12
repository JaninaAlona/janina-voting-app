"""
Django settings for vote_app_backend project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""


import os
#from pathlib import Path





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/


# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = str(os.environ.get('SECRET_KEY'))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# Application definition

INSTALLED_APPS = [
    'showvotes.apps.ShowvotesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vote_app_backend.urls'

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

WSGI_APPLICATION = 'vote_app_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    #default is an alias
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'HOST': 'vote-app-mysql',
        'PORT': '3306',
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASS'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

ALLOWED_HOSTS = [
    '*',
    '0.0.0.0',
]

CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    "http://frontend-part",
    "http://" + str(os.environ.get('DOMAIN_URL')),
    "http://*." + str(os.environ.get('DOMAIN_URL')),
    "https://127.0.0.1:8080",
    "https://localhost:8080",
    "https://frontend-part",
    "https://" + str(os.environ.get('DOMAIN_URL')),
    "https://*." + str(os.environ.get('DOMAIN_URL')),
]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    "http://frontend-part",
    "http://" + str(os.environ.get('DOMAIN_URL')),
    "http://*." + str(os.environ.get('DOMAIN_URL')),
    "https://127.0.0.1:8080",
    "https://localhost:8080",
    "https://frontend-part",
    "https://" + str(os.environ.get('DOMAIN_URL')),
    "https://*." + str(os.environ.get('DOMAIN_URL')),
]

CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    "http://frontend-part",
    "http://" + str(os.environ.get('DOMAIN_URL')),
    "http://*." + str(os.environ.get('DOMAIN_URL')),
    "https://127.0.0.1:8080",
    "https://localhost:8080",
    "https://frontend-part",
    "https://" + str(os.environ.get('DOMAIN_URL')),
    "https://*." + str(os.environ.get('DOMAIN_URL')),
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'OPTIONS',
]

# CORS_ALLOW_HEADERS = [
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
#     'Access-Control-Allow-Origin',
# ]

CORS_ALLOW_CREDENTIALS = True

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SAMESITE = 'None'
#SESSION_COOKIE_SAMESITE = 'None'
