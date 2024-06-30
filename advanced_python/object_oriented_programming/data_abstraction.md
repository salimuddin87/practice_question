## Abstract classes in Python
An abstract class can be considered a blueprint for other classes. It allows you to create a 
set of methods that must be created within any child classes built from the abstract class.

A class that contains one or more abstract methods is called an **_abstract class_**. 
An _**abstract method**_ is a method that has a declaration but does not have an implementation.

### Working on Python Abstract classes 
By default, Python does not provide abstract classes. Python comes with a module that provides 
the base for defining Abstract Base classes(ABC) and that module name is **ABC**.

ABC works by decorating methods of the base class as an abstract and then registering concrete 
classes as implementations of the abstract base. A method becomes abstract when decorated with 
the keyword **@abstractmethod**.
```python
# Python program showing
# abstract base class work
from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


# Driver code
R = Triangle()
R.noofsides()

R = Pentagon()
R.noofsides()
```

### Concrete Methods in Abstract Base Classes
```python
# Python program invoking a method using super()
from abc import ABC

class R(ABC):
    def rk(self):
        print("Abstract Base Class")

class K(R):
    def rk(self):
        super().rk()
        print("subclass ")

# Driver code
r = K()
r.rk()
```

### Abstract Properties in Python
```python
# Python program showing
# abstract properties

import abc
from abc import ABC, abstractmethod


class parent(ABC):
    @abc.abstractmethod
    def geeks(self):
        return "parent class"


class child(parent):

    @property
    def geeks(self):
        return "child class"


try:
    r = parent()
    print(r.geeks)
except Exception as err:
    print(err)

r = child()
print(r.geeks)
```
```
Output:-

Can't instantiate abstract class parent with abstract methods geeks
child class
```

### Abstract Class Instantiation
Abstract classes are incomplete because they have methods that have nobody. If Python allows 
creating an object for abstract classes then using that object if anyone calls the abstract 
method, but there is no actual implementation to invoke.

So, we use an abstract class as a template and according to the need, we extend it and build 
on it before we can use it. Due to the fact, an abstract class is not a concrete class, it 
cannot be instantiated. When we create an object for the abstract class it raises an error.

```python
# Python program showing abstract class cannot be an instantiation
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

c=Animal()
```
```
Output:-

Traceback (most recent call last):
  File "/home/ffe4267d930f204512b7f501bb1bc489.py", line 19, in 
    c=Animal()
TypeError: Can't instantiate abstract class Animal with abstract methods move
```
