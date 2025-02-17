from centurion.settings.common import *

# Turn debug off
DEBUG = True

# Allowed hosts
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', 'centuriondevelopment.net', 'www.centuriondevelopment.net', '64.23.128.107']

# Production logging will go into apaches logs
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

