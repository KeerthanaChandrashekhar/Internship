sensor_data = [

("Sensor_A", "Field_1", "Temperature", "Celsius"),

("Sensor_B", "Field_2", "Humidity", "%"),

("Sensor_C", "Field_3", "Soil Moisture", "%"),

("Sensor_D", "Field_4", "Temperature", "Celsius"),

("Sensor_E", "Field_5", "Humidity", "%")

]

#count of sensors that measure Temperature

temp_sensors = 0

for sensors in sensor_data:
    if sensors[2] == "Temperature":
        temp_sensors += 1
        
print("Number of Temperature Sensors:", temp_sensors)

#position index of humidity sensors
humidity_index = []
for i, sensors in enumerate(sensor_data):
    if sensors[2] == "Humidity":
        humidity_index.append(i)
        
print("Indices of Humidity Sensors:", humidity_index)

#display of sensor data using enumerate

for sensors, index in enumerate(sensor_data):
    print("Sensor", index + 1, "Data:", sensors)
    
    