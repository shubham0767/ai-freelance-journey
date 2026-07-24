print("=" * 30)
print("Leap Year Checker")
print("=" * 30)

year=input("Enter a year:")

if(year%400==0) or (year%4==0 and year%100!=0):
    print(f"{year}is a Leap Year.")

else:
    print(f"{year} Not a Leap Year.")    