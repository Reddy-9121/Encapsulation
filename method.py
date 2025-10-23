#Access private member outside of a class using an instance method
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private member

    def show(self):
        # Accessing private member within the class
        print("Name: ", self.name, "Salary:", self.__salary)

# Creating an instance of Employee
emp = Employee('Reddy', 10000)

# Calling the instance method to display private member
emp.show()
