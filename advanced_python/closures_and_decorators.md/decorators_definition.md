## Simple Decorator
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a 
function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped 
function, without permanently modifying it.

### Concept helpful to understand decorators

#### First Class Objects
In Python, functions are first class objects which means that functions in Python can be used or passed as arguments.

#### Properties of first class functions:
* A function is an instance of the Object type.
* You can store the function in a variable.
* You can pass the function as a parameter to another function.
* You can return the function from a function.
* You can store them in data structures such as hash tables, lists, ...

#### Example 1: Treating the functions as objects. 
```python
# Python program to illustrate functions 
# can be treated as objects 
def shout(text): 
    return text.upper() 

print(shout('Hello')) 

yell = shout 

print(yell('Hello'))
```

#### Example 2: Passing the function as an argument 
```python
# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): 
    return text.upper() 

def whisper(text): 
    return text.lower() 

def greet(func): 
    # storing the function in a variable 
    greeting = func("""Hi, I am created by a function passed as an argument.""") 
    print (greeting) 

greet(shout) 
greet(whisper)
```

```
Output:

HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
hi, i am created by a function passed as an argument.
```

#### Example 3: Returning functions from another function.
```python
# Python program to illustrate functions 
# Functions can return another function 
def create_adder(x): 
    def adder(y): 
        return x+y 

    return adder 

add_15 = create_adder(15) 

print(add_15(10))
```

## Decorators
As stated above the decorators are used to modify the behaviour of function or class. In Decorators, functions are 
taken as the argument into another function and then called inside the wrapper function.
```
Syntax for Decorator:

@gfg_decorator
def hello_decorator():
    print("Gfg")

'''Above code is equivalent to -

def hello_decorator():
    print("Gfg")
    
hello_decorator = gfg_decorator(hello_decorator)'''
```

### Decorator can modify the behaviour:  
```python
# defining a decorator
def hello_decorator(func):

    # inner1 is a Wrapper function in which the argument is called
    
    # inner function can access the outer local functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now inside the wrapper function.
        func()

        print("This is after function execution")
        
    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)


# calling the function
function_to_be_used()
```

```
Output: 

Hello, this is before function execution
This is inside the function !!
This is after function execution
```

#### find out the execution time of a function using a decorator.
```python
# importing libraries
import time
import math

# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()
        
        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function.
factorial(10)
```

#### What if a function returns something or an argument is passed to the function?
```python
def hello_decorator(func):
    def inner1(*args, **kwargs):
        
        print("before Execution")
        
        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")
        
        # returning the value to the original frame
        return returned_value
        
    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))
```

```
Output: 

before Execution
Inside the function
after Execution
Sum = 3
```
In the above example, you may notice a keen difference in the parameters of the inner function. The inner function 
takes the argument as *args and **kwargs which means that a tuple of positional arguments or a dictionary of keyword 
arguments can be passed of any length. This makes it a general decorator that can decorate a function having any 
number of arguments.

## Chaining Decorators
In simpler terms chaining decorators means decorating a function with multiple decorators.
```python
# code for testing decorator chaining 
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 

@decor1
@decor
def num(): 
    return 10

@decor
@decor1
def num2():
    return 10
  
print(num()) 
print(num2())
```

```
The above example is similar to calling the function as –

decor1(decor(num))
decor(decor1(num2))
```

#### What is the difference between wrapper and decorator in Python?
* A wrapper is the inner function defined within a decorator that actually performs the added functionality.
* A decorator is the outer function that takes a function as an argument, defines a wrapper function to modify it, and returns the wrapper.
