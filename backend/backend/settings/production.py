from decouple import config

from dj_database_url import parse as db_url

from .base import *


DEBUG = True

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['.herokuapp.com']

DATABASES = {
    'default': config('DATABASE_URL', cast=db_url),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# # Whitenoise
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# MIDDLEWARE.insert(  # insert WhiteNoiseMiddleware right after SecurityMiddleware
#     MIDDLEWARE.index('django.middleware.security.SecurityMiddleware') + 1,
#     'whitenoise.middleware.WhiteNoiseMiddleware')
