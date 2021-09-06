"""
The "hello world" custom component.

This component implements the bare minimum that a component should implement.

Configuration:

To use the hello_world component you will need to add the following to your
configuration.yaml file.

hello_world:
"""
from __future__ import annotations

from typing import Any

from homeassistant.core import HomeAssistant

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "hello_world"


def setup(hass: HomeAssistant, config: dict[str, Any]) -> bool:
    """Set up a skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.
    hass.states.set('hello_world.Hello_World', 'Works!')

    # Return boolean to indicate that initialization was successfully.
    return True
