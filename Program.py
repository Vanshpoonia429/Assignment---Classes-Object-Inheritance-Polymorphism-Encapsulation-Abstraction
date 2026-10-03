Question 5: Create a Python program with a Person class containing the person's name and a
method to display it. Then create a Student class that inherits from Person and adds the
student's course. Create an object of Student and display both details.

Answer:

Class Person:
	def __init__(self, name):
		self.name = name

	Def display_name(self):
		print(“Name:”, self.name)

Class student (person):
	def __init__(self, name, course):
		super().__init__(name)
		self.course = course

Def display_course(self):
	print(“Course:”, self.course)
student = Student(“Rauhl”, “BCA”)

student.display_name()
student.display_course()

Output:- 

Name : Rahul
Course : BCA

Question 6: Create a custom iterator class called EvenNumbers that generates even numbers
from 2 to 10.

Use __iter__(), __next__(), and StopIteration

Answer:

Class EvenNumbers:
	def __init__(self):
		self.num = 2

def __iter__(self):
		return self

def __next__(self):
		if self.num <= 10:
			value = self.num
			self.num += 2
		else:
			raise stopIteration
even = EvenNumbers()

for number in even:
	print(number)

Output:-	2
		4
		6
		8
		10



Question 7: Write a Python program using multiple inheritance. Create two classes, Teacher
and Coder, with one method in each. Create a Trainer class that inherits from both and use an
object of Trainer to call both methods.

Answer:

Class Teacher:
	def tech(self):
		print(“Teacher teaches students”)

Class coder:
	def code(self):
		print(“Coder wirtes programs”)

Class Trainer(Teacher, coder):
	pass

t = Trainer()
t.teach()
t.code()

Output:-	Teacher teaches students
		Coder writes programs



Question 8: What is polymorphism? Explain it in your own words with a Python example where
two different classes have the same method name but perform different tasks

Answer:

Polymorphism means “many forms.” In python, polymorphism allows the same method name to perform different tasks depending on the object or class that uses it.

For example, two different classes can have a method with the same name, but each class can define that method differently.

Example:-

class Dog:
	def sound(self):
		print(“Dog barks: Woof Woof”)

class Cat: 
	def sound(self):
		print(“Cat make a sound: Meow Meow”)

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

Output:-	Dog barks: Woof Woof
		Cat makes a sound: Meow Meow
Question 9: Consider the following list:

numbers = [1, 2, 3, 4, 5, 6]

Write a Python program to:

1. Use map() to calculate the square of every number.
2. Use filter() to select only even numbers.
3. Use reduce() to calculate the sum of all numbers.
4. Display all three results.

Answer:

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

#1. Calculate the square of every numbers using map()

squares = list(map(lambda x: x ** 2, numbers))

#2. Select only even numbers using filter()

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

#3. Calculate the sum of all numbers using reduce()

total = reduce(lambda x, y: x + y, numbers)

#4. Display all three results

print(“Squares:”, squares)
print(“Even numbers:”, even_numbers)
print(“Sum:”, total

Output:- 	squares: [1, 4, 9, 16, 25, 36]
		Even numbers: [2, 4, 6]
		Sum: 21


Question 10: You are developing a payment system for an online shopping application. The
system should support UPI, credit card, and wallet payments. Each payment type should have
its own way of processing the payment, but the main program should be able to call the same
pay() method for all of them. Design a simple Python solution using inheritance and
polymorphism, and explain how it works.

Answer:

Inheritance and polymorphism can be used to create a payment system where different payment methods have their own way of processing a payment, but the main program can use the same pay() method for all payment types.

class payment:
	def pay(self, amount):
		print(“Processing payment”)

class UPI(payment):
	def pay(self, amount):
		print(“Paid”, amount, “using UPI”)

class CreditCard(Payment):
	def pay(self, amount):
		print(“Paid”, amount, “using Wallet”

upi = UPI()
card = CreaditCard()
wallet = Wallet()

upi.pay(1000)
card.pay(2000)
wallet.pay(500)

Output:- 	Paid 1000 using UPI
		Paid 2000 using Credit Card
		Paid 500 using Wallet
