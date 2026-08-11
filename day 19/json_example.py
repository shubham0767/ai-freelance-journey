import json

with open("student.json", "r") as file:
    student = json.load(file)

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])