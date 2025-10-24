Types of Inheritance in Python

Types of Inheritance depend upon the number of child and parent classes involved. There are four types of inheritance in Python:


Single Inheritance :
Single inheritance enables a derived class to inherit properties from a single parent class,
thus enabling code reusability and the addition of new features to existing code.



Example:


# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")
​
# Derived class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
​
# Driver code
obj = Child()
obj.func1()
obj.func2()

Output
This function is in parent class.
This function is in child class.

Explanation:

The Child class inherits the method func1() from Parent.
It also has its own method func2().
This shows how one class can extend another using single inheritance.


Multiple Inheritance:

When a class can be derived from more than one base class this type of inheritance is called multiple inheritances.
In multiple inheritances, all the features of the base classes are inherited into the derived class.

Example:


# Base class 1
class Mother:
    mothername = ""
​
    def mother(self):
        print(self.mothername)
​
# Base class 2
class Father:
    fathername = ""
​
    def father(self):
        print(self.fathername)
​
# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
​
# Driver code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

Output
Father : RAM
Mother : SITA

Explanation:

Son inherits from both Mother and Father.
It can access both mothername and fathername.
This demonstrates how a class can combine functionalities from multiple sources.

Multilevel Inheritance:
    
In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class.
This is similar to a relationship representing a child and a grandfather.

Example:


# Base class
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
​
# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        # Call the constructor of Grandfather
        Grandfather.__init__(self, grandfathername)
​
# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        # Call the constructor of Father
        Father.__init__(self, fathername, grandfathername)
​
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)
​
# Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()

Output
Lal mani
Grandfather name : Lal mani
Father name : Rampal
Son name : Prince

Explanation:

Son inherits from Father, and Father inherits from Grandfather.
Each constructor passes values up the inheritance chain using explicit constructor calls.
All ancestor class attributes are accessible from the bottom-most class (Son).


Hierarchical Inheritance:
    
When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.
In this program, we have a parent (base) class and two child (derived) classes.

Example:


# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")
​
# Derived class 1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
​
# Derived class 2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
​
# Driver code
object1 = Child1()
object2 = Child2()
​
object1.func1()
object1.func2()
object2.func1()
object2.func3()

Output
This function is in parent class.
This function is in child 1.
This function is in parent class.
This function is in child 2.

Explanation:

Both Child1 and Child2 inherit from the same Parent class.
Each child can access the func1() method of Parent, but also has its own specific method.
This pattern is useful when multiple classes need the same base functionality but also have unique behaviors.

Hybrid Inheritance:
    
Hybrid inheritance is a combination of more than one type of inheritance. It uses a mix like single, multiple, or multilevel inheritance within the same program.
Python's method resolution order (MRO) handles such cases.

Example:

# Base class
class School:
    def func1(self):
        print("This function is in school.")
​
# Derived class 1 (Single Inheritance)
class Student1(School):
    def func2(self):
        print("This function is in student 1.")
​
# Derived class 2 (Another Single Inheritance)
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
​
# Derived class 3 (Multiple Inheritance)
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
​
# Driver code
obj = Student3()
obj.func1()
obj.func2()

Output
This function is in school.
This function is in student 1.

Explanation:

School is the base class inherited by Student1, Student2, and Student3.
Student1 and Student2 each inherit School (single inheritance).
Student3 inherits both from Student1 and School (multiple inheritance).
Python handles method resolution using the MRO, so func1() from School is resolved without ambiguity.



