counter = hass.states.get('sensor.my_counter')

if counter is None:
    value = 0
else:
    value = int(counter.state)

hass.states.set('sensor.my_counter', value + 1)
