print("=" * 35)
print("Largest Number")
print("=" * 35)

def largest(a,b,c):
    if a>=b and a>=c:
        return a

    elif b>=a and b>=c:
        return b

    else:
        return c
num1 = int(input("Enter the first Number :"))
num2 =int(input("Enter the second Number :"))
num3=int(input("Enter the third NUmber :"))

answer=largest(num1,num2,num3)

print(f"Largest Number={answer}")