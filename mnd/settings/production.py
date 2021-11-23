from __future__ import absolute_import, unicode_literals
from .base import *
import dj_database_url
import os

DATABASES=  {'default': dj_database_url.config(default='postgres://Dexter:moz1756@localhost/mnd')}
    
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'