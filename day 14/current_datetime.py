from datetime import datetime

print("=" * 40)
print("Current Date and Time")
print("=" * 40)

now = datetime.now()

print("Current Date :", now.date())
print("Current Time :", now.time())
print("Current Year :", now.year)
print("Current Month:", now.month)