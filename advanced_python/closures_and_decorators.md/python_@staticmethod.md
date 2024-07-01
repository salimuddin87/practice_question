## Python @staticmethod
A static method is a method which is bound to the class and not the object of the class. It can’t access or modify 
class state. It is present in a class because it makes sense for the method to be present in class. A static method 
does not receive an implicit first argument.
```python
# Syntax:

class C(object):
    @staticmethod
    def fun(arg1, arg2, ...):
        ...

# Returns: a static method for function fun.
```
When function decorated with @staticmethod is called, we don’t pass an instance of the class to it as it is normally 
done with methods. It means that the function is put inside the class but it cannot access the instance of that class.

#### Example #1
```python
# Python program to demonstrate static methods 
class Maths: 
	
	@staticmethod
	def addNum(num1, num2): 
		return num1 + num2 
		
# Driver's code 
if __name__ == "__main__": 
	
	# Calling method of class 
	# without creating instance 
	res = Maths.addNum(1, 2) 
	print("The result is", res)
```

```
Output:

The result is 3
```

#### Example #2
```python
# Python program to demonstrate static methods 

class Person: 
	def __init__(self, name, age): 
		self.name = name 
		self.age = age 
		
	# a static method to check if a Person is adult or not. 
	@staticmethod
	def isAdult(age): 
		return age > 18
		
# Driver's code 
if __name__ == "__main__": 
	res = Person.isAdult(12) 
	print('Is person adult:', res) 
	
	res = Person.isAdult(22) 
	print('\nIs person adult:', res)
```

```
Output:

Is person adult: False

Is person adult: True
```
