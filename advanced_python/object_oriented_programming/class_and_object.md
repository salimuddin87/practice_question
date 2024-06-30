## Classes and Objects
A class is a user-defined blueprint or prototype from which objects are created. Classes 
provide a means of bundling data and functionality together. Creating a new class creates 
a new type of object, allowing new instances of that type to be made. Each class instance 
can have attributes attached to it for maintaining its state. Class instances can also have 
methods (defined by their class) for modifying their state.
```python
# Syntax: Class Definition
class ClassName:
    # Statement


# Syntax: Object Definition
obj = ClassName()
print(obj.atrr)
```
The class creates a user-defined data structure, which holds its own data members and member 
functions, which can be accessed and used by creating an instance of that class. A class is 
like a blueprint for an object.

#### An object consists of:
1. **State:** It is represented by the attributes of an object. It also reflects the properties of an object.
2. **Behavior:** It is represented by the methods of an object. It also reflects the response of an object to other objects.
3. **Identity:** It gives a unique name to an object and enables one object to interact with other objects.

#### Self Parameter
When we call a method of this object as `myobject.method(arg1, arg2)`, this is automatically 
converted by Python into `MyClass.method(myobject, arg1, arg2)` – this is all the special 
self is about. 

#### Pass Statement
The program’s execution is unaffected by the pass statement’s inaction. It merely permits the 
program to skip past that section of the code without doing anything. It is frequently employed 
when the syntactic constraints of Python demand a valid statement but no useful code must be 
executed.

#### class `__init__()` method
The `__init__` method is similar to constructors in C++ and Java. Constructors are used to 
initializing the object’s state. Like methods, a constructor also contains a collection of 
statements(i.e. instructions) that are executed at the time of Object creation. It runs as 
soon as an object of a class is instantiated. The method is useful to do any initialization 
you want to do with your object.

#### class `__str__()` method
Python has a particular method called `__str__()`. that is used to define how a class object 
should be represented as a string. It is often used to give an object a **_human-readable textual 
representation_**, which is helpful for logging, debugging, or showing users object information. 
When a class object is used to create a string using the built-in functions print() and str(), 
the `__str__()` function is automatically used. You can alter how objects of a class are 
represented in strings by defining the `__str__()` method.

#### Class and Instance Variables
Instance variables are for data, unique to each instance and class variables are for attributes 
and methods shared by all instances of the class. Instance variables are variables whose value 
is assigned inside a constructor or method with self whereas class variables are variables whose 
value is assigned in the class.
```python
# Python3 program to show that we can create instance variables inside methods
class Dog:

    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed):
        # Instance Variable
        self.breed = breed

    # Adds an instance variable
    def setColor(self, color):
        self.color = color

    # Retrieves instance variable
    def getColor(self):
        return self.color


# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())
```
