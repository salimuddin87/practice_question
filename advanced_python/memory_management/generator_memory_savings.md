### Standard Library – Generators
* range
* dict.items
* zip
* map
* File Objects

### Use Cases of Generators
The Fundamental concept of Generator is determining the value on demand.
* Accessing Data in Pieces
* Computing Data in Pieces

A generator is an essential tool for programmers who deal with large amounts of data. Its ability to compute and 
access data on-demand results in terms of both increase in performance and memory savings. And also, consider 
using generators when there is a need to represent an infinite sequence.

### Generators for substantial memory savings in Python
When memory management and maintaining state between the value generated become a tough job for programmers, 
Python implemented a friendly solution called Generators.

With Generators, functions evolve to access and compute data in pieces. Hence, functions can return the result 
to its caller upon request and can maintain its state. Generators maintain the function state by halting the 
code after producing the value to the caller and upon request, it continues execution from where it is left off.
Since Generator access and compute value on-demand, a large chunk of data do not need to be saved in memory 
entirely and results in **substantial memory savings**.

We can say that a function is a generator when it has a **yield** statement within the code. Like in a return statement, 
the yield statement also sends a value to the caller, but it does not exit the function’s execution. Instead, it 
halts the execution until the next request is received. Upon request, the generator continues executing from where 
it is left off.
```python
def primeFunction(): 
	prime = None
	num = 1
	while True: 
		num = num + 1
		for i in range(2, num): 
			if(num % i) == 0: 
				prime = False
				break
			else: 
				prime = True

		if prime: 	
			# yields the value to the caller 
			# and halts the execution 
			yield num 

def main(): 
	# returns the generator object. 
	prime = primeFunction() 
	
	# generator executes upon request 
	for i in prime: 
		print(i) 
		if i > 50: 
			break

if __name__ == "__main__": 
	main()
```

How the caller and generator communicate with each other? 
Here we will discuss 3 in-built functions in python. They are: next, stopIteration, and send

1. **next** - The next function can request a generator for its next value. Upon request, the generator code executes 
and the yield statement provides the value to the caller.
```python
def fibonacci(): 
	values = [] 
	while True: 

		if len(values) < 2: 
			values.append(1) 
		else : 
			
			# sum up the values and 
			# append the result 
			values.append(sum(values)) 
			
			# pop the first value in 
			# the list 
			values.pop(0) 

		# yield the latest value to 
		# the caller 
		yield values[-1] 
		continue

def main(): 
	fib = fibonacci() 
	print(next(fib)) # 1 
	print(next(fib)) # 1 
	print(next(fib)) # 2 
	print(next(fib)) # 3 
	print(next(fib)) # 5 

if __name__ == "__main__": 
	main()
```

2. **stopIteration** - StopIteration is a built-in exception that is used to exit from a Generator. When the 
generator’s iteration is complete, it signals the caller by raising the StopIteration exception and it exits.
```python
def stopIteration(): 
	num = 5
	for i in range(1, num): 
		yield i 

def main(): 
	f = stopIteration() 
	
	# 1 is generated 
	print(next(f)) 
	
	# 2 is generated 
	print(next(f)) 
	
	# 3 is generated 
	print(next(f)) 
	
	# 4 is generated 
	print(next(f)) 
	
	# 5th element - raises 
	# StopIteration Exception 
	next(f) 

if __name__ == "__main__": 
	main()
```

3. **send** - allows the caller to communicate with the generator.
```python
def factorial(): 
	num = 1
	while True: 
		factorial = 1

		for i in range(1, num + 1): 
			
			# determines the factorial 
			factorial = factorial * i 
			
		# produce the factorial to the caller 
		response = yield factorial 

		# if the response has value 
		if response: 
			
			# assigns the response to 
			# num variable 
			num = int(response) 
		else: 
			
			# num variable is incremented 
			# by 1 
			num = num + 1

def main(): 
	fact = factorial() 
	print(next(fact)) 
	print(next(fact)) 
	print(next(fact)) 
	print(fact.send(5)) # send method
	print(next(fact)) 

if __name__ == "__main__": 
	main() 

```
