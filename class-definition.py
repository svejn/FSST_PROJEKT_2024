# Hier sind die benoetigten Klassen definiert

class Sensor:
    
    def __init__(self):
        self.data = []
    
    def read(self, sensor1, sensor2, sensor3):
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
        return amw_sensor_data

    def log_data(self, data1, data2, data3):
        pass

    def log_err(self, sensor1, sensor2, sensor3):
        pass


s = Sensor()
s.read("sensor1_values.txt", "sensor2_values.txt", "sensor3_values.txt")
s.calc()