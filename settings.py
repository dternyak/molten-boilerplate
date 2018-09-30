import os

from molten.contrib.toml_settings import TOMLSettings

from common import path_to

ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
SETTINGS = TOMLSettings.from_path(path_to("settings.toml"), ENVIRONMENT)


def __getattr__(name):
    return getattr(SETTINGS, name)
