from .base import DEBUG, env

# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "[{levelname}] {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {"format": "[{levelname}] {message}", "style": "{"},
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "debug_console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
            "filters": ["require_debug_true"],
        },
        # Send ERROR, CRITYCAL messages for admins if NOT DEBUG.
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["require_debug_false"],
            "formatter": "simple",
            "include_html": True,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["debug_console", "mail_admins"],
            "level": "INFO",
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["debug_console"],
            "propagate": False,
        },
        # Custom apps logger
        "apps": {
            "handlers": ["debug_console", "mail_admins"],
            "level": "DEBUG",
        },
        # Errors logged by the Sentry SDK itself
        "sentry_sdk": {
            "level": "ERROR",
            "handlers": ["debug_console"],
            "propagate": False,
        },
    },
}


# https://docs.sentry.io/platforms/python/guides/django/
# Install Sentry SDK before usage
if not DEBUG and env.bool("DJANGO_USE_SENTRY", default=False):
    import logging

    import sentry_sdk
    from sentry_sdk.integrations.celery import CeleryIntegration
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.logging import LoggingIntegration

    SENTRY_DSN = env("SENTRY_DSN")
    SENTRY_LOG_LEVEL = env.int("DJANGO_SENTRY_LOG_LEVEL", logging.INFO)

    sentry_logging = LoggingIntegration(
        level=SENTRY_LOG_LEVEL,  # Capture info and above as breadcrumbs
        event_level=logging.ERROR,  # Send errors as events
    )
    integrations = [sentry_logging, DjangoIntegration(), CeleryIntegration()]
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=integrations,
        environment=env("SENTRY_ENVIRONMENT", default="production"),
        traces_sample_rate=env.float("SENTRY_TRACES_SAMPLE_RATE", default=0.0),
    )
