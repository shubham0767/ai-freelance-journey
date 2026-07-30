print("=" * 35)
print("Append File")
print("=" * 35)

file=open("student.txt","a")

file.write("City : Mumbai\n")
file.close()
print("Data Append Successfully.\n")

file=open("student.txt","r")
print(file.read())
file.close()