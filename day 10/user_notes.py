print("=" * 35)
print("User Notes")
print("=" * 35)


note = input("Enter your note :")

file = open("notes.txt","w")

file.write(note)

file.close()

file = open("notes.txt","r")

print("\n Your Note :")
print(file.read())
file.close()
