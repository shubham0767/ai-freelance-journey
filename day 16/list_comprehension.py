print("=" * 40)
print("List Comprehension")
print("=" * 40)

numbers=[i for i in range(1,21)]

even_numbers=[ i for i in range(1,21)if i %2==0]

print("Numbers      :", numbers)
print("Even Numbers :", even_numbers)