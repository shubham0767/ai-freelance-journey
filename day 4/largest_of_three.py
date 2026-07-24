print("=" * 30)
print("Largest of Three Numbers")
print("=" * 30)

num1 = float(input("Enter First Number:"))
num2 = float(input("Enter Second Number:"))
num3 = float(input("Enter Third Number:"))

if num1>=num2 and num1>=3:
    print(f"{num1} is the Largest. ")
elif num2>=num1 and num2>=3:
    print(f"{num2} is the Largest.")
else:
    print(f"{num3} is the largest.")    