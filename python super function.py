# Python

# Parent class Company
class Company:
    # Method returning the company name
    def company_names(self):
        return "google"

# Child class Employee inheriting from Company
class Employee(Company):
    # Method to display employee info
    def info(self):
        # Call the parent method using super()
        c_name = super().company_names()
        print("Jessa works at", c_name)

# Create an instance of Employee and call info method
emp = Employee()
emp.info()
