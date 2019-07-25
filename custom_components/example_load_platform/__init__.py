"""Example Load Platform integration."""
DOMAIN = 'example_load_platform'


def setup(hass, config):
    """Your controller/hub specific code."""
    # Data that you want to share with your platforms
    hass.data[DOMAIN] = {
        'temperature': 23
    }

    hass.helpers.discovery.load_platform('sensor', DOMAIN, {}, config)

    return True
