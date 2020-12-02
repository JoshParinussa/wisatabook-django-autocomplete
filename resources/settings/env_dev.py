"""This file should contains local development defined variables.

that need to be customized
consist of (order matters):
- DJANGO
- 3rd Parties
- Applications.
"""

import os

from .application import *
from .default import *
from .thirdparty import *

# Django
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wisatabook',
        'USER': 'jopa_mysql',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    },
}


DEBUG = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{name} {levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'bolu': {
            'handlers': ['console', ],
            'level': 'DEBUG',
        }
    }
}

