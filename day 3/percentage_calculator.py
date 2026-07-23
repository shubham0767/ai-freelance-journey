print("=" * 35)
print("Student Percentage Calculator")
print("=" * 35)

sub1=float(input("enter marks for subject 1:"))
sub2=float(input("enter marks for subject 2:"))
sub3=float(input("enter marks for subject 3:"))
sub4=float(input("enter marks for subject 4:"))
sub5=float(input("enter marks for subject 5:"))

total=sub1 + sub2 + sub3 +sub4 +sub5
percentage=total/5

print("\n" + "=" *35)
print(f"Total Marks :{total}")
print(f"Percentage :{percentage:.2f} %")
if percentage >=35:
    print("Result :  Pass")
else:
    print("Result : Fail")

print("=" * 35)        