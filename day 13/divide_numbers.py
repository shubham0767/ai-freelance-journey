print("=" * 35)
print("Divide Two Numbers")
print("=" * 35)

try:
    num1=float(input("Enter First Number:"))
    num2=float(input("Enter Second Number:"))

    result=num1/num2

    print("Result =",result)

except ZeroDivisionError:
    print("Error:Cannot divide by zero.")

except ValueError:
    print("Error:Please enter valid numbers.")        