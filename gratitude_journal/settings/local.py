from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# IPs permitidas para desarrollo
INTERNAL_IPS = [
    "127.0.0.1",
]

# En desarrollo, mostrar correos en consola en lugar de enviarlos
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'