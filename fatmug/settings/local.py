from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-#q2qfpy@ij5wh_o!@2n*z#7m^(tzuk6j6*7h5^@oqnp24ia2ld",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "arshidbaba93@gmail.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "FatMug"
