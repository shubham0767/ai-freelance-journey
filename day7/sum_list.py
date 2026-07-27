print("=" * 35)
print("Sum of List")
print("=" * 35)

numbers =[]
for i in range(1,6):
    num=int(input(f"Enter Number {i}:"))
    numbers.append(num)

print("\n Numbers :", numbers)
print("Sum =",sum(numbers))
