"""Example of a custom component exposing a service."""
from __future__ import annotations

import logging

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "expose_service_sync"
_LOGGER = logging.getLogger(__name__)


def setup(hass, config) -> bool:
    """Set up the sync service example component."""
    def my_service(call) -> None:
        """My first service."""
        _LOGGER.info('Received data', call.data)

    # Register our service with Home Assistant.
    hass.services.register(DOMAIN, 'demo', my_service)

    # Return boolean to indicate that initialization was successfully.
    return True
