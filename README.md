# Assignment---Classes-Object-Inheritance-Polymorphism-Encapsulation-Abstraction
Assignment - Classes | Object | Inheritance  Polymorphism | Encapsulation | Abstraction

Topics Covered: Functions and OOPs

Question 1: What is a function in Python? Explain how functions are created and called. Also
explain parameters, arguments, default parameters, *args, and **kwargs with suitable
Examples.

Answer:

A function in Python is a reusable block of code designed to perform a specific task. Function help make program modular, readable, reusable, and easier to maintain.

Creating is created using the def keyword.

	Syntax:

Def function_name:

Example:
 
Def greet():
	print(“Hello, World!)

greet()

Output: -         Hello, World!

Parameters and Arguments

A parameters is a variable listed in function defin ation. An argument is the actual value passed to function when it is called.

Def add(a, b):
	print(a + b)
add(10, 20)

Output:-     30

Default Parameters

A default parameters has a value that is automatically used if no argument is provided for that parameters.
Def greet(name=”Guest”):
	print(“Hello”, name)
greet(“Rahul”)
greet()

Output:-    Hello Rahul
                 Hello Guest

*args

*args is used when we want a function to accept any number of positional arguments.
The arguments are received inside the function as a tuple.

Def add_numbers(*args):
	Total = 0
	For number in argos:
		Total += number

print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))

Output:-  30
               100

**Kwargs

**kwargs is used when we want a function to accept any number of keyword arguments.

The arguments are received as a dictionary.

Def student_info(**kwargs):
	For key, value in kwargs. item():
		print(key, “:”, value)

student_info(name=”Amit”, age = 20, course=”Python”)

Output:-

Name : Amit
age : 20
course : Python

Here, kwargs contain the data as a dictionary:

{
	“name” : “Amit”,
	“age” : 20,
	“Course” : “Python”
}

Using Parameters, *args, and **kwargs Together

A function can also use regular parameters, *args, and **kwargs together.

Def example(name, *args, **kwargs):
	print(“Name”:, name)
	print(“Other values:”, args)
	print(“Details:”, kwargs)

Example

(“Amit”, 10, 20, city=”Delhi”, age=21)

Output:

Name: Amit
Other values: (10, 20)
Details: {‘city’: ‘Delhi’, ‘age’:21}

Question 2: What is variable scope in Python? Explain local and global variables. Why should
excessive use of the global keyword be avoided? Also explain nested functions and closures.

Answer:

Variable Scope refers to the part of a Python program where a variable can be accessed or used. Python mainly has local scope and global scope.

1. Local Variable

A local variable is a variable created inside a function. It can only be accessed within that function.

def show():
	x = 10
	print(x)
show()

Output:-   10

2. Global Variable

A global variable is defined outside all functions. It can be accessed from different parts of the program.

x = 20

Def show():
	print(x)
show()
print(x)

Output:- 20
              20
A nested function is a function defined inside another function.

Def outer():
	Def inner():
		print(“This is the inner function.”)
inner()
outer()

Output:-   This is the inner function.

3. Closures

A clouser occurs when an inner function remembers and uses a variable from its enclosing(outer) function even after the outer function has finished executing.

def outer(x):
	def inner():
		print(x)
	return inner
function = outer(10)
function()

Output:-    10


Question 3: What is a lambda function? Explain how map(), filter(), and reduce() work in
Python with suitable examples.

Answer:

Lambda Function

A lambda function is a small, anonymous function in python. It is created using the lambda keyword and is generally used for short operations.

Syntax:

Lambda arguments: expression

Example:

square = lambda x: x * x
	print(square(5))

	Output:-   25

map() Function

The map() function applies a given function to each item of an iterable such as a list.

Syntax:

map(function, iterable)

Example:

numbers = [1, 2, 3, 4, 5]

Square = list(map(lambda x: x * x, numbers))
print(squares)

Output:- [1, 4, 9, 16, 25]

filter() Function

The filter() function selects items from an iterable based on a condition. Only item for which the function returns True are included.

Syntax: 

filter(function, iterable)

Example:-

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

Output:-     [2, 4, 6]

reduce() Function

The reduce() function repeatedly applies a function to the elements of an iterable and reduce them to a single value.

It is available in the functools module.

Example:
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

Output:- 120



Question 4:

Look at the code below and answer the questions:

class Parent:
	def show(self):
		print(“Parent”)

class Child(Parent):
	def show(self):
		print(“Child”)

obj - Child()
obj.show()

What will be printed? Why is the Parent version of show() not called?

Answer:

What will be printed?

Child

Why is the parent version of show() not called?

	This is because of method Overriding in Inheritance.

Child class inherits from Parent class.
Both class have a method with the same name and same signature show (self).
When the child class define its own implementation of a method that is already present in the parent class, it overrides the Parent’s method.
When we create an object of the child class obj = Child() and call obj.show(). Python follows the Method Resolution Order (MRO). It first searches for the method in the Child class. Since it finds show() in the child class itself, it executes that and does not go to the Parent class.
