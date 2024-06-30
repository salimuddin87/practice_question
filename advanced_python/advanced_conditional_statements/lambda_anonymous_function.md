## Python Lambda
An anonymous function means that a function is without a name. 
#### Python lambda Syntax:
```
lambda arguments : expression
```
Example 
```python
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(20))
```

### Python lambda properties:
1. This function can have any number of arguments but only one expression, which is evaluated and returned.
2. One is free to use lambda functions wherever function objects are required.
3. You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
4. It has various uses in particular fields of programming, besides other types of expressions in functions.

#### Program to demonstrate return type of Python lambda keyword 
```python
string = 'GeeksforGeeks'

# lambda returns a function object
print(lambda string: string)
```

```
Output:-
<function <lambda> at 0x7fd7517ade18>
```
**Explanation**: In this above example, the lambda is not being called by the print function, but 
simply returning the function object and the memory location where it is stored. So, to make the 
print to print the string first, we need to call the lambda so that the string will get pass the print.

#### Invoking lambda return value to perform various operations
```python
filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("Geeks101"))

do_exclaim = lambda s: s + '!'
print("do_exclaim():", do_exclaim("I am tired"))

find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum():", find_sum(101))
```
```
Output:

filter_nums(): Geeks
do_exclaim(): I am tired!
find_sum(): 2
```

#### Difference between lambda and normal function call
The main difference between lambda function and other functions defined using def keyword is that, 
we cannot use multiple statements inside a lambda function and allowed statements are also very 
limited inside lambda statements. Using lambda functions to do complex operations may affect the 
readability of the code.
```python
def cube(y):
	print(f"Finding cube of number:{y}")
	return y * y * y

lambda_cube = lambda num: num ** 3

# invoking simple function
print("invoking function defined with def keyword:")
print(cube(30))
# invoking lambda function
print("invoking lambda function:", lambda_cube(30))
```

#### The lambda function gets more helpful when used inside a function.
We can use lambda function inside map(), filter(), sorted() and many other functions.
```python
l = ["1", "2", "9", "0", "-1", "-2"]
# sort list[str] numerically using sorted()
# and custom sorting key using lambda
print("Sorted numerically:",
	sorted(l, key=lambda x: int(x)))

# filter positive even numbers
# using filter() and lambda function
print("Filtered positive even numbers:", 
	list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), l)))

# added 10 to each item after type and
# casting to int, then convert items to string again
print("Operation on each item using lambda and map()",
	list(map(lambda x: str(int(x) + 10), l)))
```

#### use lambda in list
```python
my_list = [1, 2, 3, 4, 5]

# Use lambda to filter out even numbers from the list
new_list = list(filter(lambda x: x % 2 != 0, my_list))

# Print the new list
print(new_list)
```
