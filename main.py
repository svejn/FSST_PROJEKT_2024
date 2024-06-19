import time as t
from Sensor import sensor  # Import sensor class from Sensor.py

s = sensor()
sensor_files = ["sensor1_values.txt", "sensor2_values.txt", "sensor3_values.txt"]
for i in range(10):
    s.write(sensor_files)
    s.read(sensor_files)
    s.calc()
    s.log_data()
    t.sleep(5)
