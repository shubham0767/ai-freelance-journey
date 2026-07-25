print("=" * 35)
print("Sum of First N Numbers")
print("=" * 35)

n=int(input("Enter a Number :"))
total=0
for i in range (1,n+1):
    total=total+i
print(f"Sum={total}")