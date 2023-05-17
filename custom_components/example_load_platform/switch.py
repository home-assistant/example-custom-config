"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.switch import SwitchEntity
from homeassistant.const import TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN
import logging


_LOGGER = logging.getLogger(__name__)



def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the switch platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    add_entities([MySwitch()])


class MySwitch(SwitchEntity):
    _attr_has_entity_name = True

    def __init__(self):
#         _LOGGER.info(f'turn_on.kwargs={kwargs}')
        _LOGGER.
        self._is_on = False
        self._attr_device_info ="ssxSwitchEntity_attr_device_info"  # For automatic device registration
        self._attr_unique_id = "ssxSwitchEntity_attr_unique_id"

    @property
    def is_on(self):
        """If the switch is currently on or off."""
        return self._is_on

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        self._is_on = True

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        self._is_on = False