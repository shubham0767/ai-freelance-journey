print("=" * 40)
print("Electricity Bill Calculator")
print("=" * 40)

units=float(input("Enter electricity units consumed:"))

if units<=100:
    bill=units*5

elif units <=200:
    bill = (100*5) + ((units-100)*7)

else:
    bill=(100 * 5) + (100 * 7) + ((units - 200) * 10)

print("\n" + "=" * 40)
print(f"Units Consumed : {units}")
print(f"Total Bill     : ₹{bill:.2f}")
print("=" * 40)