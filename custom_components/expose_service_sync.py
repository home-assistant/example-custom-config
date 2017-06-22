"""Example of a custom component exposing a service."""
import logging

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "expose_service_sync"
_LOGGER = logging.getLogger(__name__)


def setup(hass, config):
    """Setup the service example component."""
    def my_service(call):
        """My first service."""
        _LOGGER.info('Received data', call.data)

    # Register our service with Home Assistant.
    hass.services.register(DOMAIN, 'demo', my_service)

    # Return boolean to indicate that initialization was successfully.
    return True
