print("SIMPLE CALCULALTOR")


num1=float(input("enter your first number :"))
num2=float(input("enter your second number :"))

operation=input("choose operations(+,-,*,/):")

if operation =="+":
    print("Result=",num1 + num2)

elif operation =="_":
    print("Result=", num1 - num2)

elif operation =="*":
    print("REsult=", num1 * num2)

elif operation =="/":
    if num2!=0:
        print("Result=",num1 / num2)
    else:
        print("Error : cannot divivde by zero!")

else:
    print("Invalid operation!")        