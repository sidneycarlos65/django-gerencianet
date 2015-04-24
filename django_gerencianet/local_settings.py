import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
}

STATIC_URL = '/static/'

GERENCIANET_NOTIFICATION_URL = 'http://requestb.in/11rd2wf1'
GERENCIANET_TOKEN = '63BF2CA208349DE34632982625D69BF32163BB59'
# GERENCIANET_TOKEN = 'asdfasd'