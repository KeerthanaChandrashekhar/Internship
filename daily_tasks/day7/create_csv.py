import csv

data = [
    ["Name","Score"],
    ["Alice",85],
    ["Bob",90],
]

with open("result.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)