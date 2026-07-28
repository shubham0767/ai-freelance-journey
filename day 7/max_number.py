print("=" * 35)
print("Maximum Number")
print("=" * 35)

numbers = []
for i in range (1,6):
    num =int(input(f"Enter Number {i}:"))
    numbers.append(num)

print(f"\n Numbers:",numbers)
print("Largest Number :", max(numbers))