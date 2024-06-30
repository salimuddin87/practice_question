## Python Dictionary Comprehension
A dictionary comprehension takes the form {key: value for (key, value) in iterable}
```python
# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5] 

# but this line shows dict comprehension here 
myDict = { k:v for (k,v) in zip(keys, values)} 

# We can use below too
# myDict = dict(zip(keys, values)) 

print (myDict)
```

#### Using fromkeys() Method
```python
dic=dict.fromkeys(range(5), True)

print(dic)
# Output:- {0: True, 1: True, 2: True, 3: True, 4: True}
```

#### Using dictionary comprehension make dictionary
```python
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)
# Output:- {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

#### Using conditional statements in dictionary comprehension
```python
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)
```

#### Using nested dictionary comprehension
```python
# given string
l="GFG"

# using dictionary comprehension
dic = {
	x: {y: x + y for y in l} for x in l
}

print(dic)
# Output:- {'G': {'G': 'GG', 'F': 'GF'}, 'F': {'G': 'FG', 'F': 'FF'}}
```
