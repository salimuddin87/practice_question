## Encapsulation in Python
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
It describes the idea of wrapping data and the methods that work on data within one unit.

### Protected members
Protected members (in C++ and JAVA) are those members of the class that cannot be accessed 
outside the class but can be accessed from within the class and its subclasses. To accomplish 
this **_in Python, just follow the convention by prefixing the name of the member by a single 
underscore `“_”`._**

Although the protected variable can be accessed out of the class as well as in the derived 
class (modified too in derived class), it is customary(convention not a rule) to not access 
the protected out the class body.

```python
# Python program to demonstrate protected members 
class Base: 
	def __init__(self): 

		# Protected member 
		self._a = 2

# Creating a derived class 
class Derived(Base): 
	def __init__(self): 

		# Calling constructor of 
		# Base class 
		Base.__init__(self) 
		print("Calling protected member of base class: ", 
			self._a) 

		# Modify the protected variable: 
		self._a = 3
		print("Calling modified protected member outside class: ", 
			self._a) 


obj1 = Derived() 

obj2 = Base() 

# Calling protected member 
# Can be accessed but should not be done due to convention 
print("Accessing protected member of obj1: ", obj1._a) 

# Accessing the protected variable outside 
print("Accessing protected member of obj2: ", obj2._a)
```
```
Output: 

Calling protected member of base class:  2
Calling modified protected member outside class:  3
Accessing protected member of obj1:  3
Accessing protected member of obj2:  2
```

### Private members
Private members are similar to protected members, the difference is that the class members 
declared private should neither be accessed outside the class nor by any base class. In 
Python, there is no existence of Private instance variables that cannot be accessed except 
inside a class.

However, to define a private member prefix the member name with double underscore “__”.

**Note:** Python’s private and protected members can be accessed outside the class through 
[python name mangling](https://www.geeksforgeeks.org/private-variables-python/). 

```python
# Python program to demonstrate private members 
class Base: 
	def __init__(self): 
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"

# Creating a derived class 
class Derived(Base): 
	def __init__(self): 

		# Calling constructor of 
		# Base class 
		Base.__init__(self) 
		print("Calling private member of base class: ") 
		print(self.__c) 


# Driver code 
obj1 = Base() 
print(obj1.a) 

# Uncommenting print(obj1.c) will raise an AttributeError 

# Uncommenting obj2 = Derived() will also raise an AttributeError as 
# private member of base class is called inside derived class
```
```
Output: 

GeeksforGeeks

Traceback (most recent call last):
  File "/home/f4905b43bfcf29567e360c709d3c52bd.py", line 25, in <module>
    print(obj1.c)
AttributeError: 'Base' object has no attribute 'c'

Traceback (most recent call last):
  File "/home/4d97a4efe3ea68e55f48f1e7c7ed39cf.py", line 27, in <module>
    obj2 = Derived()
  File "/home/4d97a4efe3ea68e55f48f1e7c7ed39cf.py", line 20, in __init__
    print(self.__c)
AttributeError: 'Derived' object has no attribute '_Derived__c' 
```
