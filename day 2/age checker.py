print("=" * 30)
print("Age Category Checker")
print("=" * 30)

age=int(input("enter your age :"))
if age<18:
    print("you are minor")
elif 18 <= age <= 59:
    print("You are an Adult")
else:
    print("your are a senior citizen")    