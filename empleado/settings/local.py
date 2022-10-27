from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
   #'default': { 
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3', 
    #}
    'default': { 
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'dgit',
        'PASSWORD': 'Dgitesla0nda',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS =  [
    BASE_DIR /'static/',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'