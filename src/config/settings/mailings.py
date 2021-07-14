from .base import env

DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL", default="Backend Ecatch <noreply@ecatch.ch>"
)
FROM_EMAIL = env("DJANGO_FROM_EMAIL", default=DEFAULT_FROM_EMAIL)
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default="[Backend Ecatch]")


EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)

EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT", default=1025)
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default=None)
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default=None)
EMAIL_USE_TLS = env("EMAIL_USE_TLS", default=None)
EMAIL_TIMEOUT = 5

# https://anymail.readthedocs.io/en/stable/esps/postmark/
ANYMAIL = {
    "POSTMARK_SERVER_TOKEN": env("POSTMARK_SERVER_TOKEN", default=None),
    "POSTMARK_API_URL": env("POSTMARK_API_URL", default="https://api.postmarkapp.com/"),
}
