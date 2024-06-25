### Optimization Tips for Python Code
1. **Use built-in functions and libraries:** Builtin functions like map() are implemented in C code. So the 
interpreter doesn’t have to execute the loop, this gives a considerable speedup. The map() function applies 
a function to every member of iterable and returns the result. If there are multiple arguments, map() returns 
a list consisting of tuples containing the corresponding items from all iterables.
2. **Use keys for sorts:** In Python, we should use the key argument to the built-in sort instead, which is a 
faster way to sort.
3. **Optimizing loops:** Write idiomatic code: This may sound counter-intuitive but writing idiomatic code will 
make your code faster in most cases. This is because Python was designed to have only one obvious/correct way to 
do a task.
4. **Try multiple coding approaches:** Using precisely the same coding approach every time we create an application 
will almost certainly result in some situations where the application runs slower than it might.
5. **Use xrange instead of range:** 
   * range() – This returns a list of numbers created using range() function.
   * xrange() – This function returns the generator object that can be used to display numbers only by looping. 
   Only particular range is displayed on demand and hence called “lazy evaluation”.
6. **Use Python multiple assignment to swap variables:** This is elegant and faster in Python.
7. **Use local variable if possible:** Python is faster retrieving a local variable than retrieving a global 
variable. That is, avoid the “global” keyword. So if you are going to access a method often (inside a loop) 
consider writing it to a variable.
