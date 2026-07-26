print("=" * 35)
print("Even or Odd Checker")
print("=" * 35)

def check_even_odd(num):
    if num %2==0:
        print(f"{num} is Even.")

    else:
        print(f"{num} is Odd.")

number=int(input("Enter a number :"))
check_even_odd(number)