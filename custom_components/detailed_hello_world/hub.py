"""A demonstration 'hub' that connects several devices."""
# In a real implementation, this would be in an external library that's on PyPI.
# The PyPI package needs to be included in the `requirements` section of manifest.json
# See https://developers.home-assistant.io/docs/creating_integration_manifest
# for more information.
# This dummy hub always returns 3 rollers.
import asyncio
import random


class Hub:
    """Dummy hub for Hello World example."""

    def __init__(self, hass, host):
        """Init dummy hub."""
        self._host = host
        self._hass = hass
        self._id = host.lower()
        self.rollers = [
            Roller(f"{self._id}_1", self),
            Roller(f"{self._id}_2", self),
            Roller(f"{self._id}_3", self),
        ]
        self.online = True

    @property
    def hub_id(self):
        """ID for dummy hub."""
        return self._id

    async def test_connection(self):
        """Test connectivity to the Dummy hub is OK."""
        await asyncio.sleep(1)
        return True


class Roller:
    """Dummy roller (device for HA) for Hello World example."""

    def __init__(self, rollerid, hub):
        """Init dummy roller."""
        self._id = rollerid
        self.hub = hub
        self._callbacks = set()
        self._loop = asyncio.get_event_loop()
        self._target_position = 100
        self._current_position = 100

    @property
    def roller_id(self):
        """Return ID for roller."""
        return self._id

    @property
    def position(self):
        """Return position for roller."""
        return self._current_position

    async def set_position(self, position):
        """
        Set dummy cover to the given position.

        State is announced a random number of seconds later.
        """
        self._target_position = position
        self._loop.create_task(self.delayed_update())

    async def delayed_update(self):
        """Publish updates, with a random delay to emulate interaction with device."""
        await asyncio.sleep(random.randint(1, 10))
        await self.publish_updates()

    def registercallback(self, callback):
        """Register callback, called when Roller changes state."""
        self._callbacks.add(callback)

    # In a real implemntation, this library would call it's call backs when it was
    # notified of any state changeds for the relevant device.
    async def publish_updates(self):
        """Schedule call all registered callbacks."""
        self._current_position = self._target_position
        for callback in self._callbacks:
            self._loop.run_in_executor(None, callback)

    @property
    def online(self):
        """Roller is online."""
        # The dummy roller is offline about 10% of the time. Retuns True if online,
        # False if offline.
        return random.random() > 0.1

    @property
    def battery_level(self):
        """Battery level as a percentage."""
        return random.randint(0, 100)

    @property
    def battery_voltage(self):
        """Return a random voltage roughly that of a 12v battery."""
        return round(random.random() * 3 + 10, 2)

    @property
    def wifi_signal(self):
        """Return a sample WiFi signal strength in dB."""
        return random.randint(-90, -10)