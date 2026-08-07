print("=" * 40)
print("Fibonacci Generator")
print("=" * 40)

def fibonacci():
    a=0
    b=1

    for i in range(10):
        yield a
        a,b=b,a+b
for number in fibonacci ():
    print(number)