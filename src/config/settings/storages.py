from .aws import aws_s3_domain
from .base import BASE_DIR, env

DJANGO_USE_AWS = env.bool("DJANGO_USE_AWS", default=False)

# Static
STATIC_URL = env("DJANGO_STATIC_URL", default="/static/")
STATIC_ROOT = str(BASE_DIR / "staticfiles")
STATICFILES_DIRS = [str(BASE_DIR / "static")]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

if DJANGO_USE_AWS:
    STATICFILES_STORAGE = "backend_ecatch.utils.storages.StaticRootS3Boto3Storage"
    COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"
    STATIC_URL = f"https://{aws_s3_domain}/static/"


# Media
MEDIA_URL = env("DJANGO_MEDIA_URL", default="/media/")
MEDIA_ROOT = str(BASE_DIR / "media")

if DJANGO_USE_AWS:
    DEFAULT_FILE_STORAGE = "backend_ecatch.utils.storages.MediaRootS3Boto3Storage"
    MEDIA_URL = f"https://{aws_s3_domain}/media/"
