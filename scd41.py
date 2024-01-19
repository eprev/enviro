import time

import breakout_scd41

from enviro import i2c

breakout_scd41.init(i2c)

def get_sensor_readings():
  breakout_scd41.start()

  retries = 25
  while retries > 0 and not breakout_scd41.ready():
    time.sleep(0.2)
    retries -= 1

  if retries == 0:
    breakout_scd41.stop()
    return {}

  co2, temperature, humidity = breakout_scd41.measure()
  breakout_scd41.stop()

  from ucollections import OrderedDict
  return OrderedDict({
    "co2": co2,
    # "temperature": temperature,
    # "humidity": humidity
  })
