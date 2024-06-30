## Closures in Python

#### Nested functions in Python
A function that is defined inside another function is known as a nested function. 
Nested functions are able to access variables of the enclosing scope. 

In Python, these non-local variables can be accessed only within their scope and not outside their scope. 
This can be illustrated by the following example: 

```python
# Python program to illustrate nested functions
def outerFunction(text):

	def innerFunction():
		print(text)

	innerFunction()


if __name__ == '__main__':
	outerFunction('Hey!')
```
As we can see innerFunction() can easily be accessed inside the outerFunction body but not outside of its body. 
Hence, here, innerFunction() is treated as a nested Function that uses text as a non-local variable.

### What are Python Closures
A Closure in Python is a function object that remembers values in enclosing scopes even if they are not present in memory.
* It is a record that stores a function together with an environment: a mapping associating each free variable of the 
function (variables that are used locally but defined in an enclosing scope) with the value or reference to which the 
name was bound when the closure was created.
* A closure—unlike a plain function—allows the function to access those captured variables through the closure’s copies 
of their values or references, even when the function is invoked outside their scope.

```python
# Python program to illustrate closures 
def outerFunction(text): 

	def innerFunction(): 
		print(text) 

	# Note we are returning function
	# WITHOUT parenthesis
	return innerFunction 

if __name__ == '__main__': 
	myFunction = outerFunction('Hey!') 
	myFunction()
```
As observed from the above code, closures in Python help to invoke functions outside their scope. The function 
innerFunction has its scope only inside the outerFunction. But with the use of Python closures, we can easily 
extend its scope to invoke a function outside its scope.

```python
# Python program to illustrate closures 
import logging 
logging.basicConfig(filename='example.log',
					level=logging.INFO) 

def logger(func): 
	def log_func(*args): 
		logging.info( 
			'Running "{}" with arguments {}'.format(func.__name__,
													args)) 
		print(func(*args)) 
		
	# Necessary for closure to
	# work (returning WITHOUT parenthesis) 
	return log_func			 

def add(x, y): 
	return x+y 

def sub(x, y): 
	return x-y 

add_logger = logger(add) 
sub_logger = logger(sub) 

add_logger(3, 3) 
add_logger(4, 5) 

sub_logger(10, 5) 
sub_logger(20, 10)
```

```
~/Documents/Python-Programs/$ python MoreOnClosures.py 
Running "add" with arguments6
9
5
10

~/Documents/Python-Programs/$ cat example.log
INFO:root:Running "add" with arguments (3, 3)
INFO:root:Running "add" with arguments (4, 5)
INFO:root:Running "sub" with arguments (10, 5)
INFO:root:Running "sub" with arguments (20, 10)
```
An important thing to note here, is that we can get to know what variables are stored inside a Closure with the help 
of the `__closure__` attribute that makes use of Cell Objects to store the variables of the Outer Function and 
because of this, the closure can use these variables even when the Outer Function is terminated.

### When and Why to Use Closures
1. As Python closures are used as callback functions, they provide some sort of data hiding. This helps us to reduce the use of global variables.
2. When we have few functions in our code, closures in Python prove to be an efficient way. But if we need to have many functions, then go for class (OOP).
3. We may have variables in the global scope that are not used by many functions at times. Instead of defining variables in global scope, consider using a closure. They can be defined in the outer function and used in the inner function. Python Closures are also useful for avoiding the use of a global scope.
4. A class in the Python programming language always has the `__init__` method. If you only have one extra method, an elegant solution would be to use a closure rather than a class. Because this improves code readability and even reduces the programmer’s workload. Closures in Python can thus be used to avoid the needless use of a class.
