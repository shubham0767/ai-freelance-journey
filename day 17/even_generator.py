print("=" * 40)
print("Even Number Generator")
print("=" * 40)

def even_numbers():
    for i in range(2, 21, 2):
        yield i

for number in even_numbers():
    print(number)