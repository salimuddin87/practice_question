## Difference between iterable and iterator
An **iterable** is an object, that one can iterate over. It generates an Iterator when passed to 
iter() method. 

An **iterator** is an object, which is used to iterate over an iterable object using the `__next__()` 
method. Iterators have the `__next__()` method, which returns the next item of the object.

**_Note:_** Every iterator is also an iterable, but not every iterable is an iterator in Python.

### Example 1: 
We know that str is iterable but, it is not an iterator. where if we run this in for loop to print string 
then it is possible because when for loop executes it converts into an iterator to execute the code.
```python
next("GFG")
```
```
Output :

Traceback (most recent call last):
  File "/home/1c9622166e9c268c0d67cd9ba2177142.py", line 2, in <module>
    next("GFG")
TypeError: 'str' object is not an iterator
```

Here iter( ) is converting `s` which is a string (iterable) into an iterator and prints `G` for the first time 
we can call multiple times to iterate over strings.

When a for loop is executed, for statement calls iter() on the object, which it is supposed to loop over. 
If this call is successful, the iter call will return an iterator object that defines the method `__next__()`, 
which accesses elements of the object one at a time.        
```python
# code
s="GFG"
s=iter(s)
print(s)
print(next(s))
print(next(s))
print(next(s))
# It will throw exception because 
# there is no further elements available
print(next(s))
```
```
Output:-

<str_iterator object at 0x7f822a9c3210>
G
F
G
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

The `__next__()` method will raise a StopIteration exception if there are no further elements available. 
The for loop will terminate as soon as it catches a StopIteration exception.

### Example2: Check object is iterable or not
```python
# Function to check object is iterable or not
def it(ob):
    try:
        iter(ob)
        return True
    except TypeError:
        return False

# Driver Code
for i in [34, [4, 5], (4, 5), {"a":4}, "dfsdf", 4.5]:
    print(i,"is iterable :",it(i))
```

```
Output:-

34 is iterable : False
[4, 5] is iterable : True
(4, 5) is iterable : True
{'a': 4} is iterable : True
dfsdf is iterable : True
4.5 is iterable : False
```
