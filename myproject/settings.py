"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Paymen Integration
# PAYPAL_CLIENT_ID = 'AebLDSjPoVijQzOcl-eeAtGxybwrI9ljusfQIewCOUvxLBbHimDYcfsIUMurRdX59eEeP8NpKLO4S0mO'
# PAYPAL_SECRET_KEY = 'EGwGJ8F5Ncdkr0a0_fkl0mbkyXlEDUa2h2fT0jTQX4IiPjLtayb9zx2rmltAm8TFIpKoO80m8g4ephzH'
# PAYPAL_MODE = 'sandbox'  # 'live' for production
# PAYPAL_WEBHOOK_ID = '97G61130ER7134127'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(no1gp@#1g_ssa2*yn=jujgl=wb^es@-%vr#ekz!)6c3gde5rl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] #ngrok

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'daphne',
    'django.contrib.staticfiles',
    'myapp',
    'rest_framework',
    'paypal.standard.ipn',
    'channels',
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

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'myapp', 'templates'),],
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

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME', 'postgres'),
        'USER': os.environ.get('POSTGRES_USER','postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD','postgres'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        # 'HOST': 'db',
        # 'HOST': 'localhost',
        'PORT': '5432',
#          'TEST': {
#             'NAME': os.environ.get('POSTGRES_NAME', 'Test'),
#         },
    }
}

# PostgreSQL, pgAdmin4
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         # Docker
#         'HOST': 'db',
#         # Python
#         # 'HOST': 'localhost',
#         'PORT': '5432',
#         #  'TEST': {
#         #     'NAME': 'Test',
#         # },
#     }
# }

# EMAIL_BACKEND = 'django.core.email.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django_mail.email_backend.EmailBackend'
# EMAIL_HOST = 'smtp.example.com'
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'abiyev.rasim@gmail.com'
# EMAIL_HOST_PASSWORD = 'znem cjvv iock fbxp'

# Send Mail (Dynamic mails, attached images, invoice.pdf)
EMAIL_BACKEND = 'django_mail.email_backend.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL', 'False') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'abiyev.rasim@gmail.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'znem cjvv iock fbxp')


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# EMAIL_BACKEND = 'django.core.email.backends.console.EmailBackend'

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myapp/static')
]

# Working with image. (Watermark, Crop, Thumbnail)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Payment Integration
CSRF_TRUSTED_ORIGINS = [
    'https://0da9-185-146-113-34.ngrok-free.app',
    'https://7257-85-132-9-53.ngrok-free.app',
    'https://bcd4-185-146-113-34.ngrok-free.app',
]
PAYPAL_TEST = True
# PAYPAL_RECEIVER_EMAIL = 'sb-av0mh31470683@business.example.com'
# PAYPAL_RECEIVER_EMAIL = 'sb-qzmuw31342159@business.example.com'
# PAYPAL_RECEIVER_EMAIL = 'sb-lbdqi31794906@business.example.com'
# PAYPAL_RECEIVER_EMAIL = 'sb-vb9fz31795052@business.example.com'
PAYPAL_RECEIVER_EMAIL = 'sb-yt24f31794771@business.example.com'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Session
SESSION_ENGINE = 'django.contrib.sessions.backends.db' 
SESSION_COOKIE_NAME = 'myproject_session_id'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 3600

# login, logout
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'chat-page'
LOGOUT_REDIRECT_URL = 'login-user'
# settings.py
# LOGOUT_REDIRECT_URL = '/admin/'


# Celery, Redis
# CELERY_BROKER_URL = 'redis://myproject-redis-1:6379/0'
# CELERY_RESULT_BACKEND = 'redis://myproject-redis-1:6379/0'
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Custom User
AUTH_USER_MODEL = 'myapp.User'

# Messenger. Sockets. Chat logic.
ASGI_APPLICATION = 'myproject.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}