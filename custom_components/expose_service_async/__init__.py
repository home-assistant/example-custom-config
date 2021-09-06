"""Example of a custom component exposing a service."""
from __future__ import annotations

import asyncio
import logging

from homeassistant.core import callback

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "expose_service_async"
_LOGGER = logging.getLogger(__name__)


@asyncio.coroutine
def async_setup(hass, config) -> bool:
    """Set up the an async service example component."""
    @callback
    def my_service(call) -> None:
        """My first service."""
        _LOGGER.info('Received data', call.data)

    # Register our service with Home Assistant.
    hass.services.async_register(DOMAIN, 'demo', my_service)

    # Return boolean to indicate that initialization was successfully.
    return True
