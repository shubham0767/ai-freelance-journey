print("=" * 30)
print("Simple Calculator V2")
print("=" * 30)

num1=float(input("enter first number :"))
num2=float(input("enter second number :"))

print("\n Choose an operation:")
print("+ : ADDITION")
print("- : SUBTRACTION")
print("* : MULTIPLICATION")
print("/ : DIVISION")

choice = input("enter your choice(+,-,*,/):")
if choice =="+":
    print(f"result = {num1 + num2}")
elif choice =="-":
    print(f"result = {num1 - num2}")
elif choice =="*":
    print(f"result = {num1 * num2}")
elif choice =="/":
    if num2!=0:
        print(f"result ={num1/num2}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("invalid choice! Please select +,-,* or /.")         
