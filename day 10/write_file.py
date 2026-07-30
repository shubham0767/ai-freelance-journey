print("=" * 35)
print("Write File")
print("=" * 35)


file = open("student.txt","w")

file.write("Name : Shubham\n")
file.write("Age : 21\n")
file.write("Courses : BCA\n")

file.close()

print("Data Written Successfully .")
