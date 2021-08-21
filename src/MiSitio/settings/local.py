from .base import *  # importo todo lo que tenga base.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prestamos',
        'USER': 'postgres',
        'PASSWORD': 'Comision4',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
