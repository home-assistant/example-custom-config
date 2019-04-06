"""
Example of a custom MQTT component.

Shows how to communicate with MQTT. Follows a topic on MQTT and updates the
state of an entity to the last message received on that topic.

Also offers a service 'set_state' that will publish a message on the topic that
will be passed via MQTT to our message received listener. Call the service with
example payload {"new_state": "some new state"}.

Configuration:

To use the mqtt_example component you will need to add the following to your
configuration.yaml file.

mqtt_basic:
  topic: "home-assistant/mqtt_example"
"""
from homeassistant.components import mqtt

import voluptuous as vol

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "mqtt_basic"

CONF_TOPIC = 'topic'
DEFAULT_TOPIC = 'home-assistant/mqtt_example'

# Schema to validate the configured MQTT topic
CONFIG_SCHEMA = vol.Schema({
    vol.Optional(CONF_TOPIC, default=DEFAULT_TOPIC): mqtt.valid_subscribe_topic
})


def setup(hass, config):
    """Setup the MQTT example component."""
    topic = config[DOMAIN][CONF_TOPIC]
    entity_id = 'mqtt_example.last_message'

    # Listen to a message on MQTT.
    def message_received(topic, payload, qos):
        """A new MQTT message has been received."""
        hass.states.set(entity_id, payload)

    hass.components.mqtt.subscribe(topic, message_received)

    hass.states.set(entity_id, 'No messages')

    # Service to publish a message on MQTT.
    def set_state_service(call):
        """Service to send a message."""
        hass.components.mqtt.publish(topic, call.data.get('new_state'))

    # Register our service with Home Assistant.
    hass.services.register(DOMAIN, 'set_state', set_state_service)

    # Return boolean to indicate that initialization was successfully.
    return True
