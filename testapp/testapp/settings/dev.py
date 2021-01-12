from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kvqyqqe#x0dc#19uxg3*ipc-)%i5vt+xz@_^+cl*x39548gr*g'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += [
    'wagtail.contrib.styleguide',
    'django_extensions',
]
try:
    from .local import *
except ImportError:
    pass
