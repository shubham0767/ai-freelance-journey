print("=" * 35)
print("Shopping List")
print("=" * 35)

shopping=[]

for i  in range (1,6):
    item=input(f"Enter item {i}: ")
    shopping.append(item)

print("\n Your Shopping Lists :")

for item in shopping:
    print(item)