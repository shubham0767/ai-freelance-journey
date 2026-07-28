print("=" * 40)
print("Student Marks Manager")
print("=" * 40)

marks = []

for i in range(1,6):
    mark=float(input(f"Enter marks for Subject {i}:"))
    marks.append(mark)

total=sum(marks)
average=total/len(marks)

print("\n" + "=" * 40)
print("RESULT")
print("=" * 40)

print("Marks      :", marks)
print("Highest    :", max(marks))
print("Lowest     :", min(marks))
print("Total      :", total)
print(f"Average    : {average:.2f}")


if average >=35:
    print("Result     : Pass")
else:
    print("Result      : Fail")

print("=" * 40)