print("=" * 40)
print("Calculator")
print("=" * 40)

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:
    choice = int(input("Enter Your Choice: "))

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == 1:
        print("Answer =", num1 + num2)

    elif choice == 2:
        print("Answer =", num1 - num2)

    elif choice == 3:
        print("Answer =", num1 * num2)

    elif choice == 4:
        print("Answer =", num1 / num2)

    else:
        print("Invalid Menu Choice.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")