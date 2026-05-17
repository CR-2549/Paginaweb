"""
Django settings for hello_world project.
"""

import os
from pathlib import Path
from decouple import config
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-uroborosgaming"

DEBUG = True

ALLOWED_HOSTS = ['*']

if 'CODESPACE_NAME' in os.environ:
    codespace_name = config("CODESPACE_NAME")
    codespace_domain = config("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN")
    CSRF_TRUSTED_ORIGINS = [
        f'https://{codespace_name}-8000.{codespace_domain}'
    ]
else:
    CSRF_TRUSTED_ORIGINS = [
        'https://localhost:8000',
        'http://localhost:8000',
        'https://127.0.0.1:8000',
        'http://127.0.0.1:8000',
        'https://uroboros-gaming4.onrender.com',
    ]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "cloudinary",
    "cloudinary_storage",

    "blog",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

X_FRAME_OPTIONS = "ALLOW-FROM preview.app.github.dev"

ROOT_URLCONF = "hello_world.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "hello_world" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "hello_world.wsgi.application"

DATABASES = {
    "default": dj_database_url.parse(
        "postgresql://cristian_robles_user:Fz1OPhvhInn6fWrNi9v5LQGw6uZmk93F@dpg-d84ugvt7vvec73fioh7g-a.oregon-postgres.render.com/cristian_robles"
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATICFILES_DIRS = [
    BASE_DIR / "hello_world" / "static",
]

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "hello_world" / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "dhoo7y3oj",
    "API_KEY": "354613818298319",
    "API_SECRET": "WitSGd_FxLEqlrOpY7Zvb9iicxQ",
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"