import random
import string
print("=" * 40)
print("Password Generator")
print("=" * 40)

length=int(input("Enter Password Length : "))

characters = string.ascii_letters+string.digits

password=""

for i in range(length):
    password+=random.choice(characters)

print("Generated Password :",password)