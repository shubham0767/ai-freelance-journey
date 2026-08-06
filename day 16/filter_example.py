print("=" * 40)
print("Filter Function")
print("=" * 40)

numbers=list(range(1,21))

even = list(filter(lambda x: x % 2 == 0, numbers))
print("Original List :", numbers)
print("Even Numbers  :", even)