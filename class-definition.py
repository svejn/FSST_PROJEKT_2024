# Hier sind die benoetigten Klassen definiert

class Sensor:
    
    def __init__(self):
        pass
    
    def read(self, sensor1, sensor2, sensor3):
        """
        def DataTypeError(data):
            if data == 0:
                print("datum is zero")
                pass
            elif data != int or float:
                print("wrong datatype; datum must be integer")
        """    
        for sensor_num in range(1,4,1):
            filename = f"sensor{sensor_num}_values.txt"
            try:
                with open(filename, "r") as sensor_data:
                    data = sensor_data.read()
                    print(data)
            except FileNotFoundError:
                print("Your file was not found or doesn't exist.")
                break
            """
            except DataTypeError:
                DataTypeError(data)
            """



    def calc(self, data1, data2, data3):
        pass

    def log_data(self, data1, data2, data3):
        pass

    def log_err(self, sensor1, sensor2, sensor3):
        pass


s = Sensor()
s.read("sensor1_values.txt", "sensor2_values.txt", "sensor3_values.txt")