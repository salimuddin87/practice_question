## Python @classmethod

The classmethod() is an inbuilt function in Python, which returns a class method for a given function.

#### classmethod() in Python Syntax
```
Syntax: classmethod(function)

Parameter :This function accepts the function name as a parameter.

Return Type:This function returns the converted class method.
```

### Python classmethod() Function
The classmethod() methods are bound to a class rather than an object. 
Class methods can be called by both class and object. 

### Class Method vs Static Method
* A class method takes class as the first parameter while a static method needs no specific parameters.
* A class method can access or modify the class state while a static method can’t access or modify it.
* In general, static methods know nothing about the class state. They are utility-type methods that take some 
parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
* We use @classmethod decorator in Python to create a class method and use @staticmethod decorator to create a 
static method in Python.

### Example of Class Method:
```python
class Geeks:
    course = 'DSA'
    list_of_instances = []

    def _init_(self, name):
        self.name = name
        Geeks.list_of_instances.append(self)

    @classmethod
    def get_course(cls):
        return f"Course: {cls.course}"

    @classmethod
    def get_instance_count(cls):
        return f"Number of instances: {len(cls.list_of_instances)}"

    @staticmethod
    def welcome_message():
        return "Welcome to Geeks for Geeks!"

# Creating instances
g1 = Geeks()
g2 = Geeks()

# Calling class methods
print(Geeks.get_course())  # Course: DSA
print(Geeks.get_instance_count())  # Number of instances: 2

# Calling static method
print(Geeks.welcome_message())  # Welcome to Geeks for Geeks!
```

### Create class method using classmethod()
Created print_name classmethod before creating this line print_name() It can be called only with an object not with 
the class now this method can be called as classmethod print_name() method is called a class method.
```python
class Student:
    # create a variable
    name = "Geeksforgeeks"

    # create a function
    def print_name(obj):
        print("The name is : ", obj.name)


# create print_name classmethod
# before creating this line print_name()
# It can be called only with object not with class
Student.print_name = classmethod(Student.print_name)

# now this method can be called as classmethod
# print_name() method is called a class method
Student.print_name()
```

### Factory method using a Class method
Uses of classmethod() function are used in factory design patterns where we want to call many functions with the 
class name rather than an object.
```python
# Python program to demonstrate
# use of a class method and static method.
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    def display(self):
        print("Name : ", self.name, "Age : ", self.age)

person = Person('mayank', 21)
person.display()
```

### How the class method works for the inheritance?
```python
from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def from_FathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def from_BirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Female'

man = Man.from_BirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.from_FathersAge('John', 1965, 20)
print(isinstance(man1, Man))
```

```
Output:

True
False
```

## Python @classmethod Decorator
The @classmethod decorator is a built-in function decorator which is an expression that gets evaluated after your 
function is defined. The result of that evaluation shadows your function definition. A class method receives the 
class as the implicit first argument, just like an instance method receives the instance.

#### Syntax of classmethod Decorator
```
class C(object):  

   @classmethod

      def fun(cls, arg1, arg2, …):

       ….

Where,
    fun: the function that needs to be converted into a class method
    returns: a class method for function.
```

#### Note:
* A class method is a method that is bound to the class and not the object of the class.
* They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
* It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that would be applicable to all instances.

```python
# Python program to demonstrate
# use of a class method and static method.
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
```

```
Output:

21
27
True
```

## Is `__new__` a class method?
Yes, `__new__` is a class method, but it is not defined with the @classmethod decorator. It is a special method in 
Python that is used to create a new instance of a class. `__new__` is called before `__init__` and is responsible 
for returning a new instance of the class.

When you call a class to create an instance, `__new__` is the method that actually allocates memory for the new 
object. It is then followed by the `__init__` method to initialize the instance.

Example:
```python
class MyClass:
    def __new__(cls):
        print("Creating a new instance")
        return super().__new__(cls)  # Create and return a new instance

    def __init__(self):
        print("Initializing the instance")

obj = MyClass()
# Output:
# Creating a new instance
# Initializing the instance
```

## What is `__str__` class method in Python?
`__str__` is a special method used to define the string representation of an object. It is not technically a 
class method but an instance method. When you use print() or str() on an instance of the class, the `__str__` 
method is called to produce a human-readable string representation of the object.

You can override `__str__` to provide a meaningful string output for instances of your class.

Example:
```python
class MyClass:
    def __str__(self):
        return "This is MyClass instance"

obj = MyClass()
print(obj)  # Output: This is MyClass instance
```

## What is the difference between a method and a class method?
* Method or Instance Method:
  * Instance Method: Takes self as the first parameter. It is used to access or modify instance attributes and can call other instance methods.
  * Example:
```python
class MyClass:
    def instance_method(self):
        return "This is an instance method"
```

* Class Method:
  * Class Method: Takes cls as the first parameter. It is used to access or modify class state that applies across all instances.
  * Decorated with: @classmethod
  * Example:
```python
class MyClass:
    @classmethod
    def class_method(cls):
        return "This is a class method"
```

## What is the @classmethod decorator in Python?
The @classmethod decorator defines a method that is bound to the class and not the instance. It allows you to call 
the method on the class itself or on instances of the class. The first parameter of a class method is cls, which 
refers to the class and not the instance.

Example:
```python
class MyClass:
    @classmethod
    def class_method(cls):
        return f"This is a class method of {cls.__name__}"

print(MyClass.class_method())  # Output: This is a class method of MyClass
```
