students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None },
]

name = input("Name: ").lower()

for student in students:
    print(student["name"])

for student in students:
    if name == student["name"].lower():
        print(student["name"])

  