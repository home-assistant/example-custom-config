"""Example Load Platform integration."""
from __future__ import annotations

from typing import Any

from homeassistant.core import HomeAssistant

DOMAIN = 'example_load_platform'


def setup(hass: HomeAssistant, config: dict[str, Any]) -> bool:
    """Your controller/hub specific code."""
    # Data that you want to share with your platforms
    hass.data[DOMAIN] = {
        'temperature': 23
    }

    hass.helpers.discovery.load_platform('sensor', DOMAIN, {}, config)

    return True
