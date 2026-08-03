print("=" * 35)
print("Safe Number Input")
print("=" * 35)

try:
    number = int(input("Enter an Integer: "))
    print("You entered:", number)

except ValueError:
    print("Please enter a valid integer.")