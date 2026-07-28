print("=" * 40)
print("Student Database")
print("=" * 40)

student={}

student["Name"] = input("Enter Name: ")
student["Age"] = int(input("Enter Age: "))
student["City"] = input("Enter City: ")
student["College"] = input("Enter College: ")
student["Course"] = input("Enter Course: ")
student["Phone Number"] = input("Enter Phone Number: ")

print("\n" + "=" * 40)
print("STUDENT DATABASE")
print("=" * 40)

for key, value in student.items():
    print(f"{key:<13}: {value}")

print("=" * 40)