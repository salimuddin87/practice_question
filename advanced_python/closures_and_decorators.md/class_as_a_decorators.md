## Class as a Decorator in Python
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of 
function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped 
function, without permanently modifying it.

We can define a decorator as a class in order to do that, we have to use a `__call__` method of classes. When a 
user needs to create an object that acts as a function then function decorator needs to return an object that acts 
like a function, so `__call__` can be useful. For Example
```python
# Python program showing use of __call__() method
class MyDecorator:
	def __init__(self, function):
		self.function = function
	
	def __call__(self):

		# We can add some code before function call

		self.function()

		# We can also add some code after function call.


# adding class decorator to the function
@MyDecorator
def function():
	print("GeeksforGeeks")

function()
```

```
Output: 

GeeksforGeeks
```

### Class Decorator with *args and **kwargs 
In order to use class decorator with argument *args and **kwargs we used a `__call__` function and passed both the 
argument in a given function
```python
# Python program showing class decorator with *args and **kwargs

class MyDecorator:
	def __init__(self, function):
		self.function = function
	
	def __call__(self, *args, **kwargs):

		# We can add some code before function call

		self.function(*args, **kwargs)

		# We can also add some code after function call.
	

# adding class decorator to the function
@MyDecorator
def function(name, message ='Hello'):
	print("{}, {}".format(message, name))

function("geeks_for_geeks", "hello")
```

```
Output: 

hello, geeks_for_geeks
```

### Class Decorator with return statement
In the given example the functions did not return anything so there is not any issue, but one may need the returned 
value. So we use return statement with the class decorator. 
```python
# Python program showing class decorator with return statement

class SquareDecorator:

	def __init__(self, function):
		self.function = function

	def __call__(self, *args, **kwargs):

		# before function
		result = self.function(*args, **kwargs)

		# after function
		return result

# adding class decorator to the function
@SquareDecorator
def get_square(n):
	print("given number is:", n)
	return n * n

print("Square of number is:", get_square(195))
```

```
Output:
 
given number is: 195
Square of number is: 38025
```

### Using class Decorators to print Time required to execute a program 
In order to print time required to execute a program, we use `__call__` function and use a time module so that we 
can get an execute time of a program 
```python
# Python program to execute time of a program

# importing time module
from time import time
class Timer:

	def __init__(self, func):
		self.function = func

	def __call__(self, *args, **kwargs):
		start_time = time()
		result = self.function(*args, **kwargs)
		end_time = time()
		print("Execution took {} seconds".format(end_time-start_time))
		return result


# adding a decorator to the function
@Timer
def some_function(delay):
	from time import sleep

	# Introducing some time delay to simulate a time taking function.
	sleep(delay)

some_function(3)
```

### Checking error parameter using class decorator 
This type of class decorator is most frequently used. This decorator checks parameters before executing the function 
preventing the function to become overloaded and enables it to store only logical and necessary statements.
```python
# Python program checking error parameter using class decorator
class ErrorCheck:

	def __init__(self, function):
		self.function = function

	def __call__(self, *params):
		if any([isinstance(i, str) for i in params]):
			raise TypeError("parameter cannot be a string !!")
		else:
			return self.function(*params)


@ErrorCheck
def add_numbers(*numbers):
	return sum(numbers)

# returns 6
print(add_numbers(1, 2, 3)) 

# raises Error. 
print(add_numbers(1, '2', 3))
```

```
Output : 

6
TypeError: parameter cannot be a string !!
```
