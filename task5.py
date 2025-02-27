class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"Salary increased by ₱{amount:,.2f}. New salary: ₱{self.salary:,.2f}")

    def display_employee(self):
        print(f"Employee: {self.name}, Position: {self.position}, Salary: ₱{self.salary:,.2f}")

employee = Employee("Anastasha Knight", "Data Analyst", 441740)

employee.display_employee()
employee.give_raise(38392)
employee.display_employee()
