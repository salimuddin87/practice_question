In Python, Assignment statements do not copy objects, they create bindings between a target and an object. 
When we use the = operator, It only creates a new variable that shares the reference of the original object. 
In order to create “real copies” or “clones” of these objects, we can use the copy module in Python.

#### Syntax of Python Deepcopy
```
import copy

y = copy.deepcopy(x)
``` 

#### Syntax of Python Shallowcopy
```
import copy

y = copy.copy(x)
```

### What is Deep copy in Python?
A deep copy creates a new compound object before inserting copies of the items found in the original into it in a 
recursive manner. It means first constructing a new collection object and then recursively populating it with copies 
of the child objects found in the original. In the case of deep copy, a copy of the object is copied into another 
object. **It means that any changes made to a copy of the object do not reflect in the original object.**
```python
import copy
li1 = [1, 2, [3,5], 4]
li2 = copy.deepcopy(li1)
print ("The original elements before deep copying")
for i in range(0,len(li1)):
	print (li1[i],end=" ")

print("\r")
li2[2][0] = 7
print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
	print (li2[i],end=" ")

print("\r")
print ("The original elements after deep copying")
for i in range(0,len( li1)):
	print (li1[i],end=" ")
```
```
Output:

The original elements before deep copying
1 2 [3, 5] 4 
The new list of elements after deep copying 
1 2 [7, 5] 4 
The original elements after deep copying
1 2 [3, 5] 4 
```

### What is Shallow copy in Python?
A shallow copy creates a new compound object and then references the objects contained in the original within it, 
which means it constructs a new collection object and then populates it with references to the child objects found 
in the original. The copying process does not recurse and therefore won’t create copies of the child objects 
themselves. In the case of shallow copy, a reference of an object is copied into another object. It means that any 
changes made to a copy of an object do reflect in the original object. 
In python, this is implemented using the “copy()” function.
```python
import copy
li1 = [1, 2, [3,5], 4]
li2 = copy.copy(li1)
print ("The original elements before shallow copying")
for i in range(0,len(li1)):
	print (li1[i],end=" ")

print("\r")
li2[2][0] = 7
print ("The original elements after shallow copying")
for i in range(0,len( li1)):
	print (li1[i],end=" ")
```
```
Output:

The original elements before shallow copying
1 2 [3, 5] 4 
The original elements after shallow copying
1 2 [7, 5] 4 
```
### Example
```python
import copy


if __name__ == '__main__':
    a = [1, 3, 2, [1, 2], 5]
    b = a  # by default shallow copy i.e. [1, 3, 2, [1, 2], 5]
    b[3].append(3)
    print(b)  # pointing to same object i.e. [1, 3, 2, [1, 2, 3], 5]
    print(a)  # [1, 3, 2, [1, 2, 3], 5]

    c = copy.deepcopy(a)
    print(c)  # [1, 3, 2, [1, 2, 3], 5]

    c.append(6)
    print(c)  # [1, 3, 2, [1, 2, 3], 5, 6]
    print(a)  # [1, 3, 2, [1, 2, 3], 5]

    c[3].append(4)
    print(c)  # [1, 3, 2, [1, 2, 3, 4], 5, 6]
    print(a)  # [1, 3, 2, [1, 2, 3], 5]

    d = copy.copy(a)
    print(d)  # [1, 3, 2, [1, 2, 3], 5]

    d.append(6)
    print(d)  # [1, 3, 2, [1, 2, 3], 5, 6]
    print(a)  # [1, 3, 2, [1, 2, 3], 5]

    d[3].append(4)
    print(d)  # [1, 3, 2, [1, 2, 3, 4], 5, 6]
    print(a)  # [1, 3, 2, [1, 2, 3, 4], 5]
```
