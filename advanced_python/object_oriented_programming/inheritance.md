## Inheritance in Python
One of the core concepts in object-oriented programming (OOP) languages is inheritance. 
It is a mechanism that allows you to create a hierarchy of classes that share a set of 
properties and methods by deriving a class from another class. Inheritance is the capability 
of one class to derive or inherit the properties from another class. 

#### Benefits of inheritance are:
1. It represents real-world relationships well.
2. It provides the re-usability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
3. It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
4. Inheritance offers a simple, understandable model structure.
5. Less development and maintenance expenses result from an inheritance. 

#### Python Inheritance Syntax
The syntax of simple inheritance in Python is as follows:
```
Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}
```

#### A Python program to demonstrate inheritance 
```python
class Person(object): # object is by default used when not mentioned

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True


# Driver code
emp = Person("Geek1") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())
```

### The super() Function
The super() function is a built-in function that returns the objects that represent the parent 
class. It allows to access the parent class’s methods and attributes in the child class.

```python
# parent class
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name, self.age)


# child class
class Student(Person):
    def __init__(self, name, age):
        self.sName = name
        self.sAge = age
        # inheriting the properties of parent class
        super().__init__("Rahul", age)
        
    def displayInfo(self):
        print(self.sName, self.sAge)


obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()
```

### Different types of Python Inheritance
There are 5 different types of inheritance in Python. They are as follows:
1. **_Single inheritance:_** When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.
2. _**Multiple inheritances:**_ When a child class inherits from multiple parent classes, it is called multiple inheritances.
3. **_Multilevel inheritance:_** When we have a child and grandchild relationship. This means that a child class will inherit from its parent class, which in turn is inheriting from its parent class.
4. **_Hierarchical inheritance:_** More than one derived class can be created from a single base.
5. **_Hybrid inheritance:_** This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.

#### Private members of the parent class
We don’t always want the instance variables of the parent class to be inherited by the child 
class i.e. we can make some of the instance variables of the parent class private, which won’t 
be available to the child class. 

In Python inheritance, we can make an instance variable private by adding double underscores 
before its name. For example:
```python
# Python program to demonstrate private members of the parent class
class C(object):
	def __init__(self):
		self.c = 21

		# d is private instance variable
		self.__d = 42


class D(C):
	def __init__(self):
		self.e = 84
		C.__init__(self)

object1 = D()

# produces an error as d is private instance variable
print(object1.c)
print(object1.__d)
```
