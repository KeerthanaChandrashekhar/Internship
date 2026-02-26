import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Grade"] != "F":
            print(f"Name: {row['Name']}, Grade: {row['Grade']}")