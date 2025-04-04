squares = [ x ** 2 for x in range(10) if x % 2 == 0 ]
print(squares)


# Mapping numbers to their clubes
cubes = {x: x**3 for x in range(5)}
print(cubes)

# Unique lengths of words

words = ["hello", "world", "python", "hello"]
unique_lengths = {len(word) for word in words}
print(unique_lengths)

# Generates look like list comprehensions but use parentheses. They compute values lazily, making them memory-efficient

squares_gen = (x**2 for x in range(5))
for square in squares_gen:
    print(square)

# Comprehensions can be nested for multi-dimesntional data processing

matrix = [[1,2], [3,4],[5,6]]
flattened = [num for row in matrix for num in row]
print(flattened)

name = "Guido"
level = "advanced"
print(f"{name} is an {level} Python Programmer!")

# Combine expression directly
age = 30
print(f"In 10 years, I will be {age +10} years old")

# Use f-string to format numbers with precision or in human-reachable fromats
pi = 3.14159
print(f"Pi rounded to two decimal: {pi:.2f}")

# Add thousands separators
large_number = 123456789
print(f"large number with commas: {large_number:,}")

# Display Percentages:
success_rate = 0.874
print(f"Success rate: {success_rate:.1%}")


# Use f-strings with datetime objects for cleaner formatter

from datetime import datetime

now = datetime.now()
print(f"Current date: {now:%Y-%m-%d}")
print(f"Current time: {now:%H-%M-%S}")

# Allign text for neately formatted outputs

name = "Python"
print(f"{name:<10} is left-aligned")
print(f"{name:>10} is right-aligned")
print(f"{name:^10} is centered")

#F-strings support a debugging syntax that displays botht the expression and its result
value = 42
print(f"{value=}")
print(f"{value+30=}")

###############################
# Brilliant.org
#

##############################
# Python build in function
#

# you can use enumerate to loop through an iterable while keeping tracak of the index
items = ['apple', 'banana', 'cherry']
for index, item in enumerate(items, start=1):
    print(f"{index}: {item}")

# zip, which combines two or more iterables element-wise, crearting tuples
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# any and all are also quite useful
numbers = [1, 0, 1, 1]
print(any(numbers))     # Output: True (at least one non-zero)
print(all(numbers))      # Output: False (not all are non-zero)

# map transforms an iterable by applying a function to each element
numbers = [1,2,3,4]
squares = map(lambda x: x * 2, numbers)
print(list(squares))

# Use filter to select elements based on a condition
numbers = [10, 15, 20, 25, 30]
divisible_by_10 = filter(lambda x: x % 10 == 0, numbers)
print(list(divisible_by_10))

# Use reversed to reverse an iterable without modifying it
items = ['apple', 'banana', 'cherry']
for item in reversed(items):
    print(item)

#Did you know min and max also work with customer keys?
words = ["apple", "banana", "cherry"]
longest_word = max(words, key=len)
print(f"The longest word is {longest_word} with {len(longest_word)} characters")

######################
# Use Generator
#

# A generator function that yields square numbers
def square_numbers(limit: int):
    for n in range(limit):
        yield n * n

# use the generator function to compute values
for square in square_numbers(5):
    print(square)


# import time
# # A generator that computes the square of numbers with a delay

# def delayed_squares(limit):
#     for n in range(limit):
#         print(f"Computing square for: {n}")
#         time.sleep(1)   # Simulate a delay in computation
#         yield n * n

# # instantiate the generator
# gen = delayed_squares(3)

# # Step through the generator manually
# print("Fecthinhg values on the fly:")
# print(next(gen)) # Compute square of 0
# print(next(gen)) # Compute square of 1
# print(next(gen)) # Comput square of 2

########################
# Use Context Manager
#

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# Context mangers can help manage external connections like databases, ensuring they close properly

# import sqlite3
# with sqlite3.connect("example.db") as conn:
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
#     cursor.execute("INSERT INTO users (id, name) VALUES (1, 'Alice')")
#     conn.commit()
#     cursor.execute("SELECT * FROM users")
#     print(cursor.fetchall())

# The connection is automatically closed at the end of the block.

# you can create your own context manager using generators with @contextmanager

# import time
# from contextlib import contextmanager

# @contextmanager
# def timer():
#     start = time.time()
#     yield
#     end = time.time()
#     print(f"Elapsed time: {end - start:.2f} seconds")

# # Usage
# with timer():
#     total = sum(range(10_000_000))
#     print(f"Sum computed: {total}")

# For more complex scenarios, implement the __enter__ and __exit__ methods directly in a class

# class CustomResources:
#     def __enter__(self):
#         print("Resource acquired")
#         return self
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Resource relased")

# with CustomResources() as resource:
#     print("Using the resource")

#########################
# Use the Python Eco System
#
import httpx

reponse = httpx.get("https://api.github.com")
print(reponse.status_code)
print(reponse.json()) 

###########
# use type annotations
#

# Type hints help others understand your code better

def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)

print(average([10,20,30]))

# Type hints also help you write code that's more generic:

from typing import Iterable

def average(numbers: Iterable[int]) -> float:
    return sum(numbers) / len(numbers)

print(average([10, 20, 30]))

#######################
# Use Abstraction
# 

# Decoupling the Code 
# ABC is used in Python
# Abstraction using ABCs:

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount} payment via Paypal.")

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount} payment via Stripe.")

def process_order(amount: float, processor: PaymentProcessor) -> None:
    processor.process_payment(amount)

paypal = PayPalProcessor()
stripe = StripeProcessor()

process_order(100.0, paypal)
process_order(200.0, stripe)


# Abstracting a logger using a protocol:

# Python Duct Typing Mehcanisam

from typing import Protocol

class Logger(Protocol):
    def log(self, message: str) -> None:
        pass

class ConsoleLogger:
    def log(self, message: str) -> None:
        print(f"LOG: {message}")

class FileLogger:
    def log(self, message: str) -> None:
        with open("log.txt", "a") as file:
            file.write(f"{message}\n")

def perform_task(logger: Logger) -> None:
    logger.log("Task Started")
    #Simulate a task
    logger.log("Task Completed")

console_logger = ConsoleLogger()
file_logger = FileLogger()
perform_task(console_logger) # Output: LOG: Task Started. LOG: Task Completed
perform_task(file_logger) # Logs to a File


####################
# Write Test
# 

# Pytest

#########################
# Classes and function
#

from decimal import Decimal

class ShoppingCart:
    def __init__(self) -> None:
        self.items = []

    def add_item(self, item: str, price: Decimal) -> None:
        self.items.append({'item': item, 'price': price})
    
    def total(self) -> Decimal:
        return sum(item['price'] for item in self.items)
    
cart = ShoppingCart()

cart.add_item("apple", Decimal("1.5"))
cart.add_item("banana", Decimal("2.0"))
print(f"${cart.total():.2f}")

# A dataclass is a lightweight alternative to a class.it's perfect for scenarios where you need a group related data but don't need much behaviour

from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Item:
    name: str
    price: Decimal

item = Item(name="apple", price=Decimal("1.5"))
print(item)
print(f"${item.price:.2f}")


## Use a function for stateless operations: tasks that don't require maintaining state over time and can be performed independently.

def calculated_discounted_price(price: Decimal, discount: Decimal) -> Decimal:
    return price - (price * discount / 100)

discounted_price = calculated_discounted_price(Decimal("100"), Decimal("10"))
print(f"${discounted_price:.2f}")
