### Reference counting
Reference counting works by counting the number of times an object is referenced by other objects 
in the system. When references to an object are removed, the reference count for an object is decremented. 
When the reference count becomes zero, the object is deallocated.

For example, Let’s suppose there are two or more variables that have the same value, so, what Python 
virtual machine does is, rather than creating another object of the same value in the private heap, 
it actually makes the second variable point to that originally existing value in the private heap. 
Therefore, in the case of classes, having a number of references may occupy a large amount of space 
in the memory, in such a case referencing counting is highly beneficial to preserve the memory to be 
available for other objects

```python
x = 10 
```
When x = 10 is executed an integer object 10 is created in memory and its reference is assigned to 
variable x, this is because everything is object in Python.
```python
x = 10
y = x 

if id(x) == id(y): 
	print("x and y refer to the same object") 
```
Output: x and y refer to the same object

In the above example, y = x will create another reference variable y which will refer to the same object 
because Python optimizes memory utilization by allocation the same object reference to a new variable if 
the object already exists with the same value.
![alt text](C:\Users\md_salimuddin_ansari\PycharmProjects\practice_question\advanced_python\memory_management\memory-allocation-python-2.jpg)

Now, let’s change the value of x and see what happens.
```python
x = 10
y = x 
x += 1

if id(x) != id(y): 
	print("x and y do not refer to the same object") 
```
Output: x and y do not refer to the same object

So now x refer to a new object x and the link between x and 10 disconnected but y still refer to 10
![](C:\Users\md_salimuddin_ansari\PycharmProjects\practice_question\advanced_python\memory_management\memory-allocation-python-1.jpg)

There are two parts of memory:
* stack memory
* heap memory

The methods/method calls and the references are stored in stack memory and all the values objects are 
stored in a private heap(a portion of the computer's memory dedicated to the Python interpreter).

### Work of Stack Memory
The allocation happens on contiguous blocks of memory. We call it stack memory allocation because the allocation 
happens in the function call stack. The size of memory to be allocated is known to the compiler and whenever a 
function is called, its variables get memory allocated on the stack.

It is the memory that is only needed inside a particular function or method call. When a function is called, it 
is added onto the program’s call stack. Any local memory assignments such as variable initializations inside the 
particular functions are stored temporarily on the function call stack, where it is deleted once the function 
returns, and the call stack moves on to the next task. This allocation onto a contiguous block of memory is handled 
by the compiler using predefined routines, and developers do not need to worry about it.
```python
def func(): 
	# All these variables get memory 
	# allocated on stack 
	a = 20
	b = [] 
	c = ""
```

### Work of Heap Memory (Dynamic allocation and de-allocation)
The memory is allocated during the execution of instructions written by programmers. Note that the name heap has 
nothing to do with the heap data structure. It is called heap because it is a pile of memory space available to 
programmers to allocated and de-allocate. The variables are needed outside of method or function calls or are 
shared within multiple functions globally are stored in Heap memory.
```python
# This memory for 10 integers 
# is allocated on heap. 
a = [0]*10
```

### List memory management
Lists in Python are dynamic arrays, which means they can grow or shrink in size as needed. When a list is created, 
Python allocates a certain amount of memory to accommodate the initial elements. As the list grows, additional memory 
is allocated to accommodate more elements. when elements are added to the list using the append method, Python may 
need to allocate additional memory to accommodate the new elements.

Python also has a mechanism for deallocating memory that is no longer in use, known as garbage collection. When 
elements are removed from a list, the memory occupied by those elements may be deallocated, freeing up resources.

### Tuple memory management
Tuples, unlike lists, are immutable, meaning their size and elements cannot be changed after creation. This 
immutability has implications for memory management. When a tuple is created, Python allocates a fixed amount of 
memory to accommodate all the elements.

Since tuples are immutable, elements cannot be added or removed from them. As a result, there is no need for memory 
de-allocation. Once a tuple is created, the allocated memory remains fixed for the lifetime of the tuple.
