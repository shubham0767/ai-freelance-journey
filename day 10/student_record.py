print("=" * 40)
print("Student Record Saver")
print("=" * 40)

name=input("Enter your Name :")
age=int(input("Enter your Age :"))
city=input("Enter your city :")
college = input("Enter your college :")
course = input("Enter your Course :")

file=open("students_records.txt","a")

file.write("--------------------------\n")
file.write(f"Name    : {name}\n")
file.write(f"Age     : {age}\n")
file.write(f"City    : {city}\n")
file.write(f"College : {college}\n")
file.write(f"Course  : {course}\n")
file.write("--------------------------\n")

file.close()
print("\n Record Saved Successfully!\n")

file=open("students_records.txt","r")

print(file.read())

file.close()