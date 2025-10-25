from datetime import date

class Person:
    # Initialize the person object with a name, country, and date of birth
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    # Calculate the age of the person based on their date of birth
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

# Create a person object with valid date
person1 = Person("Reddy", "Darsi", date(2005, 12, 11)) 
# Access and print the attributes and calculated age for the person
print("Calculated age for each person")
print("******************************")
print("Person 1:")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.date_of_birth)
print("Age:", person1.calculate_age())


OUTPUT:

Calculated age for each person
******************************
Person 1:
Name: Reddy
Country: Darsi
Date of Birth: 2005-12-11
Age: 19
