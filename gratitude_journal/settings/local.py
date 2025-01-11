from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# IPs permitidas para desarrollo
INTERNAL_IPS = [
    "127.0.0.1",
]