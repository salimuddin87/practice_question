## Private variables in Python
There is no existence of “Private” instance variables that cannot be accessed except inside an 
object. However, a convention is being followed by most Python code and coders i.e., a name 
prefixed with an underscore, For e.g. _geek should be treated as a non-public part of the API 
or any Python code, whether it is a function, a method, or a data member

#### Mangling and how it works
Any identifier of the form `__geek` (at least two leading underscores or at most one trailing 
underscore) is replaced with `_classname__geek`, where classname is the current class name with 
a leading underscore(s) stripped. As long as it occurs within the definition of the class, this 
mangling is done. 

This is helpful for letting subclasses override methods without breaking intraclass method calls.
The mangling rules are designed mostly to avoid accidents but, it is still possible to access or 
modify a variable that is considered private. This can even be useful in special circumstances, 
such as in the debugger.

### _Single Leading Underscores
So basically one underline at the beginning of a method, function, or data member means you 
shouldn’t access this method because it’s not part of the API.

```python
# Python code to illustrate how single underscore works
def _get_errors(self):
	if self._errors is None:
		self.full_clean()
	return self._errors

errors = property(_get_errors)
```

### __Double Leading Underscores

```python
# Python code to illustrate how double underscore at the beginning works
class Geek:
	def _single_method(self):
		pass
	def __double_method(self): # for mangling
		pass
class Pyth(Geek):
	def __double_method(self): # for mangling
		pass
```

### \__Double leading and Double trailing underscores\__
There’s another case of double leading and trailing underscores. We follow this while using 
special variables or methods **_(called “magic method”)_** such as `__len__`, `__init__`. These 
methods provide special syntactic features to the names. For example, `__file__` indicates the 
location of the Python file, `__eq__` is executed when a == b expression is executed. 
