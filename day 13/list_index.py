print("=" * 35)
print("List Index Checker")
print("=" * 35)

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

try:
    index = int(input("Enter Index (0-4): "))
    print("Fruit:", fruits[index])

except IndexError:
    print("Error: Index out of range.")

except ValueError:
    print("Error: Please enter a valid integer.")


    