"""
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
"""
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": reader})
    
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")