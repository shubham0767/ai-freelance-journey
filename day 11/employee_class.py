print("=" * 35)
print("Employee Class")
print("=" * 35)

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("\n Emplyoee Details ")
        print("Name : ",self.name)
        print("ID   : ", self.emp_id)
        print("Salary : ",self.salary)

name=input("Enter Name :")       
emp_id=input("Enter ID  : ")
salary=input("Enter Salary:")
emp=Employee(name,emp_id,salary)

emp.display