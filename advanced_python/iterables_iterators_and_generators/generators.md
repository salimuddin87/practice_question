## Generators in Python
A Generator in Python is a function that returns an iterator using the Yield keyword.

#### Create a Generator
```
def function_name():
    yield statement 
```

```python
# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
	yield 1			
	yield 2			
	yield 3			

# Driver code to check above generator function 
for value in simpleGeneratorFun(): 
	print(value)
```

### Generator Object
Python Generator functions return a generator object that is iterable, i.e., can be used as an Iterator. 
Generator objects are used either by calling the next method of the generator object or using the generator 
object in a “for in” loop.

```python
# A Python program to demonstrate use of generator object with next() 
# A generator function 
def simpleGeneratorFun(): 
	yield 1
	yield 2
	yield 3

# x is a generator object 
x = simpleGeneratorFun() 

# Iterating over the generator object using next 

# In Python 3, __next__() 
print(next(x)) 
print(next(x)) 
print(next(x))
```

We will create two generators for Fibonacci Numbers, first a simple generator and second generator using a for loop.
```python
# A simple generator for Fibonacci Numbers 
def fib(limit): 
	
	# Initialize first two Fibonacci Numbers 
	a, b = 0, 1

	# One by one yield next Fibonacci Number 
	while a < limit: 
		yield a 
		a, b = b, a + b 

# Create a generator object 
x = fib(5) 

# Iterating over the generator object using next 
# In Python 3, __next__() 
print(next(x)) 
print(next(x)) 
print(next(x)) 
print(next(x)) 
print(next(x)) 

# Iterating over the generator object using for in loop. 
print("\nUsing for in loop") 
for i in fib(5): 
	print(i)
```

```
Output:-

0
1
1
2
3

Using for in loop
0
1
1
2
3
```

### Python Generator Expression
In Python, generator expression is another way of writing the generator function. It uses the Python list 
comprehension technique but instead of storing the elements in a list in memory, it creates generator objects.

```
Generator Expression Syntax:- 

    (expression for item in iterable)
```

```python
# generator expression 
generator_exp = (i * 5 for i in range(5) if i%2==0) 

for i in generator_exp: 
	print(i)
```

```
Output:

0
10
20
```

### Applications of Generators in Python 
Suppose we create a stream of Fibonacci numbers, adopting the generator approach makes it trivial; we just have 
to call next(x) to get the next Fibonacci number without bothering about where or when the stream of numbers ends. 

A more practical type of stream processing is handling large data files such as log files. Generators provide a 
space-efficient method for such data processing as only parts of the file are handled at one given point in time. 
We can also use Iterators for these purposes, but Generator provides a quick way (We don’t need to write `__next__` 
and `__iter__` methods here).
