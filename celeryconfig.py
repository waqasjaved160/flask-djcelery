import os

DEBUG = True
PROJECT_DIR = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'NAME': 'celerybeat.db',
        'ENGINE': 'django.db.backends.sqlite3',
    },
}
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'djcelery',
    'rest_framework'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}

SECRET_KEY = 'SomeSecretKey!'
ROOT_URLCONF = 'urls'
STATIC_URL = '/static/'

# Celery configuration
BROKER_URL = 'redis://localhost:6379/0'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
