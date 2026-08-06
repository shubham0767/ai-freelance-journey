from functools import reduce

print("=" * 40)
print("Reduce Function")
print("=" * 40)

numbers = [10, 20, 30, 40, 50]

total = reduce(lambda x, y: x + y, numbers)

print("Numbers :", numbers)
print("Total Sum =", total)