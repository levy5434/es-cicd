import os  # NOQA

from .settings import *  # NOQA

IS_CI = os.getenv("GITHUB_ACTIONS") == "true"

print(f"IS CI: {IS_CI}")

if IS_CI:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("TEST_DB_NAME", "test_db"),
            "USER": os.getenv("TEST_DB_USER", "test_user"),
            "PASSWORD": os.getenv("TEST_DB_PASSWORD", "test_pass"),
            "HOST": os.getenv("TEST_DB_HOST", "localhost"),
            "PORT": os.getenv("TEST_DB_PORT", "5432"),
        }
    }
else:
    DATABASES = {
        "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
    }
