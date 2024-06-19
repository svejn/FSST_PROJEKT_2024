import time as t
from Sensor import sensor  # Import sensor class from Sensor.py
import threading
import time 
import matplotlib.animation

s = sensor()
sensor_files = ["sensor1_values.txt", "sensor2_values.txt", "sensor3_values.txt"]

def run(frame):
    print("stuff happenss")
    s.write(sensor_files)
    s.read(sensor_files)
    new_value= s.calc()
    s.update_plot(new_value)
    print(new_value)
    s.log_data()

s.run_plot(run, 300)