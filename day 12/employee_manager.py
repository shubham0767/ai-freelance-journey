print("=" * 40)
print("Employee and Manager")
print("=" * 40)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print("\nManager Details")
        print("=" * 40)
        print("Name       :", self.name)
        print("Salary     :", self.salary)
        print("Department :", self.department)

manager = Manager("Shubham", 60000, "IT")

manager.display()