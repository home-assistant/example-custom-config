"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN
import logging
import random



_LOGGER = logging.getLogger(__name__)

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    add_entities([ExampleSensor()])


class ExampleSensor(SensorEntity):
    """Representation of a sensor."""

    def __init__(self) -> None:
        """Initialize the sensor."""
        self._state = None
        self._attr_device_info ="ssxSensorEntity_attr_device_info"  # For automatic device registration
        self._attr_unique_id = "ssxSensorEntity_attr_unique_id"

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return 'Example Temperature'

    @property
    def state(self):
        """Return the state of the sensor."""
        _LOGGER.info('state ExampleSensor !')
        return self._state

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        _LOGGER.info('unit_of_measurement ExampleSensor !')
        return TEMP_CELSIUS

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        _LOGGER.info('update ExampleSensor !')
        # self._state = self.hass.data[DOMAIN]['temperature']
        self._state = random.randint(-20,99)
