print("=" * 40)
print("Calculator Using Functions")
print("=" * 40)

def add(a,b):
    return a +b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a *b
def divide(a,b):
    if b !=0:
        return a/b
    else:
        return "Cannot divide by zero "

num1=float(input("Enter first number:"))
num2=float(input("Enter second number :"))

print("\n choose an operation :")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1-4):")

if choice=="1":
    print("Result=",add(num1,num2))

elif choice == "2":
    print("Result =",subtract(num1,num2))

elif choice=="3":
    print("Result =",multiply(num1,num2))

elif choice=="4":
    print("Result =", divide(num1,num2))

else:
    print("Invalid Choice !")    