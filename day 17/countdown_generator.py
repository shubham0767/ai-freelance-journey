print("=" * 40)
print("Countdown Generator")
print("=" * 40)

def countdown(start):
    while start >=1:
        yield start 
        start -=1
number=int(input("enter starting number :"))

for i in countdown(number):
    print()
print("Done!")
