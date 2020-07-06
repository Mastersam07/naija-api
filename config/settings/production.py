
from config.settings.base import *

import dj_database_url


MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    *MIDDLEWARE
]

ALLOWED_HOSTS = [
    '.herokuapp.com'
]

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
