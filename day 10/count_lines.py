print("=" * 35)
print("Count Lines")
print("=" * 35)

file=open("student.txt","r")

lines=file.readlines()

print("Total Lines :", len(lines))

file.close()