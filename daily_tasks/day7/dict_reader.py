import csv

with open("stud_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Age"])
        

with open("stud_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)