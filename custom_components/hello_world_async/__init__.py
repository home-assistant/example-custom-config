"""
The "hello world" custom component.

This component implements the bare minimum that a component should implement.

Configuration:

To use the hello_word component you will need to add the following to your
configuration.yaml file.

hello_world_async:
"""
import asyncio

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "hello_world_async"


@asyncio.coroutine
def async_setup(hass, config):
    """Setup our skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.
    hass.states.async_set('hello_world_async.Hello_World', 'Works!')

    # Return boolean to indicate that initialization was successfully.
    return True
