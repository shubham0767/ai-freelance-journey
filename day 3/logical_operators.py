age=int(input('enter the age:'))
citizen=input("Are you an Indian citizen ? (yes/no) :").lower()
if age >=18 and citizen =="yes":
    print("Eligible to vote")
else:
    print("Not eligible to vote")