from .base import DEBUG

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "storages",
    "anymail",
]
LOCAL_APPS = ["apps.authentication.apps.AuthenticationConfig"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

DEVELOPMENT_APPS = ["django_extensions"]

if DEBUG:
    INSTALLED_APPS += DEVELOPMENT_APPS
