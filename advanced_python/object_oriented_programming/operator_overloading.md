## Operator Overloading in Python
Operator Overloading means giving extended meaning beyond their predefined operational meaning. 
For example operator + is used to add two integers as well as join two strings and merge two 
lists. It is achievable because ‘+’ operator is overloaded by int class and str class. 
```python
# Python program to show use of + operator for different purposes.

print(1 + 2)

# concatenate two strings
print("Geeks"+"For") 

# Product two numbers
print(3 * 4)

# Repeat the String
print("Geeks"*4)
```
```
Output
3
GeeksFor
12
GeeksGeeksGeeksGeeks
```

#### Overloading binary + operator in Python: 
```python
# Python Program illustrate how to overload an binary + operator And how it actually works
class A:
	def __init__(self, a):
		self.a = a

	# adding two objects 
	def __add__(self, o):
		return self.a + o.a 
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)

# Actual working when Binary Operator is used.
print(A.__add__(ob1 , ob2)) 
print(A.__add__(ob3,ob4))

#And can also be Understand as :
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))
```
```
Output:-

3
GeeksFor
3
GeeksFor
3
GeeksFor
```

#### Binary Operators:
Operator    |	Magic Method
------------|--------------
+   |	`__add`__(self, other)
– |	`__sub`__(self, other)
* |	`__mul`__(self, other)
/ |	`__truediv`__(self, other)
// |	`__floordiv`__(self, other)
% |	`__mod`__(self, other)
** |	`__pow`__(self, other)
\>> |	`__rshift`__(self, other)
<< |	`__lshift`__(self, other)
& |	`__and`__(self, other)
\| |	`__or`__(self, other)
^ |	`__xor`__(self, other)

#### Comparison Operators:
Operator |	Magic Method
---------|--------------
< |	`__lt`__(self, other)
\> |	`__gt`__(self, other)
<= |	`__le`__(self, other)
\>= |	`__ge`__(self, other)
== |	`__eq`__(self, other)
!= |	`__ne`__(self, other)

#### Assignment Operators:
Operator |	Magic Method
---------|---------------
-= |	`__isub`__(self, other)
+= |	`__iadd`__(self, other)
*= |	`__imul`__(self, other)
/= |	`__idiv`__(self, other)
//= |	`__ifloordiv`__(self, other)
%= |	`__imod`__(self, other)
**= |	`__ipow`__(self, other)
\>>= |	`__irshift`__(self, other)
<<= |	`__ilshift`__(self, other)
&=	| `__iand`__(self, other)
\!= |	`__ior`__(self, other)
^= |	`__ixor`__(self, other)

#### Unary Operators:
Operator |	Magic Method
---------|--------------
– |	`__neg`__(self)
+ |	`__pos`__(self)
~ |	`__invert`__(self)
