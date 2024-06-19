import datetime as dt
import time as t 
import random as r
import matplotlib.pyplot as plt
import matplotlib.axes as  axis
import matplotlib.animation as animation
from collections import deque


class sensor:
    
    def __init__(self):
        self.data = []
        self.sensor_am = []

        deque_length=10
        y_range=(0,10)

        self.plotdata=deque([0]*deque_length,deque_length)
        self.ax: axis.Axes
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(self.plotdata)
        
        #self.ax.set_ylim(y_range)
        self.ax.set_xlim(0, deque_length - 1)
        self.deque_length=deque_length


    def write(self, sensor_files): # only serves a demonstrational purpous, as there are no real sensor values
        for filename in sensor_files:
            random_value = r.randint(1, 15)
            with open(filename, "a") as sensor_file:
                sensor_file.write(f"{random_value}\n")
                sensor_file.close()

    def read(self, sensor_files):
        self.data = []  # Clear previous data
        for filename in sensor_files:
            try:
                with open(filename, "r") as sensor_data:
                    data_r = sensor_data.read().split()
                    data_r = [int(item) for item in data_r]
                    self.data.append(data_r)
            except FileNotFoundError:
                #print(f"File {filename} was not found or doesn't exist.")
                self.log_err(f"File {filename} was not found or doesn't exist.")
        #print(self.data)

    def calc(self):
        if not self.data:
            print("No data available to calculate")
            return None
        sum_data = 0
        len_data = 0

        for sensor_index, sublist in enumerate(self.data): # enumerate() gives index-values to sensor (sublists in this case)
            cons_zeros = 0  # counts consecutive 0-values for each sensor
            for item in sublist:
                if item == 0: 
                    cons_zeros += 1
                    if cons_zeros > 3:
                        self.log_err(f"Sensor {sensor_index + 1} may be defect. No values received in the last 15 sec.")
                else:
                    cons_zeros = 0  # 0-counter back to 0
                sum_data += item
                len_data += 1

        amw_sensor_data = sum_data / len_data if len_data > 0 else 0
        #print(f"Arithmetic Mean: {amw_sensor_data}")
        self.sensor_am.append(amw_sensor_data)

        #print("this is in sensor_am:", self.sensor_am)

        return amw_sensor_data


    
    def update_plot(self,new_value: int):
        self.plotdata.append(new_value)
        print(self.plotdata)
        
        # Update the line data
        self.line.set_ydata(self.plotdata)
        
        # Update the x-axis ticks and labels
        self.ax.set_xticks(range(len(self.plotdata)))
        self.ax.set_xticklabels([f't-{i}' if i != 0 else 't' for i in range(self.deque_length - 1, -1, -1)])

        self.ax.relim()
        self.ax.autoscale_view(scaley=True, scalex=False)

    def run_plot(self, run_func, interval):
        self.ani = animation.FuncAnimation(self.fig, run_func, interval=interval)
        plt.show()

    def log_data(self):
        if self.sensor_am:
            log_time = dt.datetime.now().strftime("Date: %Y-%m-%d ||| Time: %H:%M:%S")
            last_am = self.sensor_am[-1]
            with open("data_log.txt", "a") as sensor_log_file:
                sensor_log_file.write(f"{log_time}  |||  {len(self.data)} Sensors active  |||   AM:{last_am}\n")
            
    def log_err(self, message):
        log_time = dt.datetime.now().strftime("Date: %Y-%m-%d ||| Time: %H:%M:%S")
        with open("error_log.txt", "a") as error_log_file:
            error_log_file.write(f"{log_time}  |||  ERROR: {message}\n")