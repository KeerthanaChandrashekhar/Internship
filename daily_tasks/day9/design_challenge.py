sensors = [
    ("S1", "Field_A", "Temperature", "Celsius"),
    ("S2", "Field_B", "Humidity", "%"),
    ("S3", "Field_C", "Temperature", "Celsius"),
    ("S4", "Field_D", "Pressure", "Pascal"),
]

#Count how many sensors measure "Temperature"
temp_count = sum(1 for s in sensors if s[2] == "Temperature")
print("Temperature sensors:", temp_count)

#Find the position (index) of "Humidity" in any metadata tuple
for s in sensors:
    if "Humidity" in s:
        print("Index of 'Humidity' in tuple:", s.index("Humidity"))

#Display all sensor metadata using enumerate()
print("\nAll sensor metadata:")
for i, s in enumerate(sensors):
    print(i, s)

#Print the number of fields in each metadata tuple
print("\nNumber of fields in each tuple:")
for s in sensors:
    print(len(s))

#Use unpacking to print readable sentence
print("\nReadable descriptions:")
for name, location, parameter, unit in sensors:
    print(f"Sensor {name} located at {location} measures {parameter} in {unit}.")
