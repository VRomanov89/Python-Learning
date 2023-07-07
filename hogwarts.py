students = ["Hermoine", "Harry", "Ron"]

for student in students:
    print (student)

for i in range(len(students)):
    print(i + 1, students[i])

# Dictionary - keys / values

students2 = {
    "Hermoine": "Gryff", 
    "Harry": "Gryff",
    "Draco": "Slyth",
}

print(students2["Hermoine"])

for student in students2:
    print(student, students2[student])

students3 = [
    {"name": "Hermoine", "house": "Gryff", "patron": "Otter"},
    {"name": "Harry", "house": "Gryff", "patron": "Stag"},
    {"name": "Draco", "house": "Slyth", "patron": None}
]

for student in students3:
    print(student["name"], student["house"], student["patron"], sep=", ")

#Exceptions in Python
