import os
from .base import *

# Variable de entorno para determinar el entorno
DJANGO_ENV = os.getenv('DJANGO_ENV', 'development')

if DJANGO_ENV == 'production':
    from .production import *
else:
    from .local import *