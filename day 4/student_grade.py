print("=" * 35)
print("Student Grade System")
print("=" * 35)

marks=float(input("Enter your Marks (0-100):"))

if marks<0 or marks>100:
     print("Invalid marks! Please enter marks between 0 and 100.")

elif marks>=90:
     print("Grade : A+")
     print("Result : Pass")

elif marks>=80:
     print("Grade : A")
     print("Result : Pass")

elif marks>=70:
     print("Grade : B")
     print("Result : Pass")     

elif marks>=60:
     print("Grade : C")
     print("Result : Pass") 

elif marks >= 50:
    print("Grade  : D")
    print("Result : Pass")

elif marks >= 35:
    print("Grade  : E")
    print("Result : Pass")

else:
    print("Grade  : F")
    print("Result : Fail")

print("=" * 35)     
