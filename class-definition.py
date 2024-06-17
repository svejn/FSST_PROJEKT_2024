# Hier sind die benoetigten Klassen definiert
import datetime as dt
import time as t 

class Sensor:
    
    def __init__(self):
        self.data = []
        self.sensor_am = []

    def read(self, sensor1, sensor2, sensor3):
        global sensor_num
        for sensor_num in range(1, 4):
            filename = f"sensor{sensor_num}_values.txt"
            try:
                with open(filename, "r") as sensor_data:
                    data_r = sensor_data.read().split()
                    data_r = [int(item) for item in data_r]
                    self.data.append(data_r)
                #print(f"Data from {filename}: {data_r}")

            except FileNotFoundError:
                print(f"File {filename} was not found or doesn't exist.")
                break
        print(self.data)

    def calc(self):
        if not self.data:
            print("No data available to calculate")
            return None
        sum_data = 0
        len_data = 0
        for sublist in self.data:
            for item in sublist:
                sum_data += item
                len_data += 1
            #print(sublist)
        print(sum_data)
        amw_sensor_data = sum_data / len_data
        print(f"Arithmetic Mean: {amw_sensor_data}")
        self.sensor_am.append(amw_sensor_data)
        print("this is in sensor_am:", self.sensor_am)

    def log_data(self):
        log_time = dt.datetime.now().strftime("%Y-%m-%d|%H:%M:%S")
        sensor_log_data = map(str, self.sensor_am)
        data_to_write = str(list(sensor_log_data))
        with open("data_log.txt", "a") as sensor_log_file:
            sensor_log_file.write(f"Date|Time: {log_time}  |||  {sensor_num} Sensors acitve  |||   AM:{data_to_write}"+ "\n")
            

    def log_err(self, sensor1, sensor2, sensor3):
        pass


s = Sensor()
s.read("sensor1_values.txt", "sensor2_values.txt", "sensor3_values.txt")
s.calc()
for i in range(1,10,1):
    s.log_data()
    t.sleep(5)