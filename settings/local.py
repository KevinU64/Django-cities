from .base import *
import pymysql

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#pymysql.version_info = {1, 4, 3, 'final', 0}

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'codigo_facilito',
        'USER': 'root',
        'PASSWORD': '2001125',
        'HOST': 'localhost',
        'PORT': ''
    }
}