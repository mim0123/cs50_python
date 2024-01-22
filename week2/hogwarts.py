students = [
    {"name": "hermione", "house": "gryffindor","patronus": "otter"},
    {"name": "harry", "house": "gryffindor","patronus": "stag"},
    {"name": "ron", "house": "gryffindor","patronus": "dog"},
    {"name": "draco", "house": "gryffindor","patronus": None},

    
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")