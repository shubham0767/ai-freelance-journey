print("=" * 35)
print("Employee Details")
print("=" * 35)

name=input("Enter Employee Name :")
emp_id = input("Enter Employee ID :")
department=input("Enter Department :")
salary=float(input("Enter Salary :"))

employee={
    "Name" :name,
    "ID" : emp_id,
    "Department " : department,
    "salary": salary,

}
print("\n Employee Information")
print("="*50)

for key,value in employee.items():
    print(f"{key} :{value}")