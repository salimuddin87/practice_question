## Python – List Comprehension
A Python list comprehension consists of brackets containing the expression, which is executed for 
each element along with the for loop to iterate over each element in the Python list. 
```python
numbers = [12, 13, 14,] 
doubled = [x *2 for x in numbers] 
print(doubled)
```

```python
list = [i for i in range(11) if i % 2 == 0] 
print(list)
```

#### Advantages of List Comprehension
1. More time-efficient and space-efficient than loops.
2. Require fewer lines of code.
3. Transforms iterative statement into a formula.

### Matrix using List Comprehension
```python
matrix = [[j for j in range(3)] for i in range(3)] 
print(matrix)
```

### List Comprehensions vs For Loop
```python
# Empty list 
List = [] 

# Traditional approach of iterating 
for character in 'Geeks 4 Geeks!': 
	List.append(character) 

# Display list 
print(List)
```

Above is the implementation of the traditional approach to iterate through a list, string, tuple, etc. 
Now, list comprehension in Python does the same task and also makes the program more simple. 

List Comprehensions translate the traditional iteration approach using for loop into a simple formula 
hence making them easy to use. Below is the approach to iterate through a list, string, tuple, etc. 
using list comprehension in Python.

```python
# Using list comprehension to iterate through loop 
List = [character for character in 'Geeks 4 Geeks!'] 

# Displaying list 
print(List)
```

### Time Analysis in List Comprehensions and Loop
The list comprehensions in Python are more efficient both computationally and in terms of coding space 
and time than a for a loop. Typically, they are written in a single line of code. The below program 
depicts the difference between loops and list comprehension based on performance.
```python
# Import required module 
import time 


# define function to implement for loop 
def for_loop(n): 
	result = [] 
	for i in range(n): 
		result.append(i**2) 
	return result 


# define function to implement list comprehension 
def list_comprehension(n): 
	return [i**2 for i in range(n)] 


# Driver Code 

# Calculate time taken by for_loop() 
begin = time.time() 
for_loop(10**6) 
end = time.time() 

# Display time taken by for_loop() 
print('Time taken for_loop:', round(end-begin, 2)) 

# Calculate time takens by list_comprehension() 
begin = time.time() 
list_comprehension(10**6) 
end = time.time() 

# Display time taken by for_loop() 
print('Time taken for list_comprehension:', round(end-begin, 2))
```

```
Output:-

Time taken for_loop: 0.68
Time taken for list_comprehension: 0.48
```

### Nested List Comprehensions
A list comprehension within another list comprehension which is quite similar to nested for loops.
```python
matrix = [] 

for row in range(3): 
	# Append an empty sublist inside the list 
	matrix.append([]) 

	for col in range(5): 
		matrix[row].append(col) 

print(matrix)
```

```
Output:-
[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
```

```python
# Nested list comprehension 
matrix = [[j for j in range(5)] for i in range(3)] 

print(matrix)
```

```
Output:-
[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
```

### List Comprehensions and Lambda

```python
# List comprehension to print table of 10
numbers = [i*10 for i in range(1, 6)] 

print(numbers) 

# using lambda to print table of 10 
numbers = list(map(lambda i: i*10, [i for i in range(1, 6)])) 

print(numbers)
```

### Conditionals in List Comprehension
We can also add conditional statements to the list comprehension. We can create a list using range(), 
operators, etc. and cal also apply some conditions to the list using the if statement.

#### using if-else statement
```python
lis = ["Even number" if i % 2 == 0
	else "Odd number" for i in range(8)] 
print(lis)
```

#### using nested if
```python
lis = [num for num in range(100) 
	if num % 5 == 0 if num % 10 == 0] 
print(lis)
```

#### Transpose of the matrix using list comprehension.
```python
twoDMatrix = [[10, 20, 30], 
			[40, 50, 60], 
			[70, 80, 90]] 

# Generate transpose 
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix[0]))] 

print(trans)
```

#### Reverse each string in a Tuple
```python
# Reverse each string in tuple 
List = [string[::-1] for string in ('Geeks', 'for', 'iter')] 

# Display list 
print(List)
# Output:-  ['skeeG', 'rof', 'reti']
```

#### Creating a list of Tuples from two separate Lists
```python
names = ["G", "G", "g"] 
ages = [25, 30, 35] 
person_tuples = [(name, age) for name, age in zip(names, ages)] 
print(person_tuples)
# Output:- [('G', 25), ('G', 30), ('g', 35)]
```
