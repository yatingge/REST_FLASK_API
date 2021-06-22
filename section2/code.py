# 1. lambda function, short functins ofter using without a name
def add(x, y):
	return x + y

add = lambda x, y : x + y  # keyword paramters : return value
# print(add(4, 5))
# (lambda x, y : x + y)(5, 7) # not very ofter

def double(x):
	return x ** 2

seq = [1, 2, 3, 5]
doubled = list(map(lambda x: x * 2, seq)) # map(func, iterable), return generator 
# print(doubled)

# 2. unpacking arguments
def multiply(*args): # tuple of mutiple arguments
	total = 1
	for arg in args:
		total = total * arg
	return total

a = multiply(1, 3, 5)

def add(x, y):
	return x + y
nums = [3, 5]
# print(add(*nums))
nums = {'x': 15, 'y': 25}
# print(add(**nums)) # dictonary where keys must be same as named arguments

def apply(*args, operator):
	if operator == '*':
		return multiply(*args)
	elif operator == '+':
		return sum(args)
	else:
		return 'No valid'

# print(apply(1,3,4,7, operator='+'))
# print(apply(1,3,4,7, operator='*'))

# 3. unpacking keyword arguments
def named1(**kwargs): ## keyword arguments, dictionary
	print(kwargs)

# named1(name='Bob', age=25) # collected as a key-value dictionary

def named2(name, age):
	print(name, age)
detail = {'name': 'bob', 'age':23}
# named2(**detail)

# 4. Object-oriented programming in Python
class Student:
	def __init__(self):
		self.name = 'Rolf'

student = Student()

# 5. magic methods, __str__ and __repr__ # do not need to call it by yourself
# 6. class methods and static methods
class ClassTest:
	def instance_method(self):
		print(f"Called instance_method of {self}")

	@classmethod
	def class_method(cls): # class itself
		print(f"Called class_method of {cls}")

	@staticmethod
	def static_method(): # usually no argument
		print("Called static_method")

test = ClassTest() # an instance of class object
# test.instance_method()
# ClassTest.class_method() # do not need class object
# ClassTest.static_method()

# example
class Book:
	TYPES = ('Hardcover', 'paperback') 

	def __init__(self, name, book_type, weight):
		self.name = name
		self.book_type = book_type
		self.weight = weight

	def __repr__(self):
		return f"<Book {self.name}, {self.book_type}, weighting {self.weight} g>"

	@classmethod
	def hardcover(cls, name, page_weight):
		return cls(name, cls.TYPES[0], page_weight + 100)

	@classmethod
	def paperback(cls, name, page_weight):
		return Book(name, Book.TYPES[1], page_weight + 100)


book1 = Book.hardcover('Harry Potter', 1500)
book2 = Book.paperback('Harry, Potter', 1400)

# 7. class inheritance # printer is a device
class Device:
	def __init__(self, name, connected_by):
		self.name = name
		self.connected_by = connected_by
		self.connected = True

	def __str__(self):
		return f'Device {self.name!r} ({self.connected_by})'

	def disconnect(self):
		self.connected = False
		print("Disconnected")


class Printer(Device): # inheritance
	def __init__(self, name, connected_by, capacity):
		super().__init__(name, connected_by) # parent class
		self.capacity = capacity
		self.remaining_pages = capacity

	def __str__(self):
		return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

	def print(self, pages):
		if not self.connected:
			print("Your printer is not connected")
			return 
		print(f'Printing {pages} pages')
		self.remaining_pages -= pages

# printer = Printer("Printer", "USB", 500)
# printer.print(20)
# printer.disconnect()
# printer.print(20)

# 8. class composition bookshelf contains many books
class BookShelf:
	def __init__(self, *books):
		self.books = books

	def __str__(self):
		return f'BookShelf with {len(self.books)} books.'

shelf = BookShelf(300)
class Book: 
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f'Book {self.name}'

book1 = Book("aaa")
book2 = Book("bbb")
shelf = BookShelf(book1, book2)

# 9. Type hinting 
from typing import List

def list_avg(sequence : List) -> float:
	return sum(sequence) / len(sequence)

# 10. error
# 11. first class functions -> functions are variables
def divide(dividend, divisor):
	if divisor == 0:
		raise ZeroDivisionError("Divisor cannot be 0")
	return dividend / divisor

def calculate(*values, operator):
	return operator(*values)

result = calculate(20, 4, operator=divide) # passing a function as parameter
# print(result)

# 12. Simple decorator in Python 
user = {"username": "Jose", "access_level": "guest"}

from functools import wraps

def make_secure(func):
	# decorator 
	# @functools.wraps(func)
	def secure_function(*args, **kwargs): # inner function 
		if user['access_level'] == 'admin':
			return func(*args, **kwargs)
		else:
			return 'No password'

	return secure_function

@make_secure # decorators
def get_admin_password():
	return '1234'

# print(get_admin_password())

# 13. mutability 
a = [4]
b = a[:]
a += [5]
print(a)
print(b)


