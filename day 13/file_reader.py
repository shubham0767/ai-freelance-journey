print("=" * 35)
print("File Reader")
print("=" * 35)

filename=input("Enter File Name :")
try:
    file=open(filename,"r")
    print("\nFile Content:\n")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error:File not found")