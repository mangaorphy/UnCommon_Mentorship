"""
==============================================
WEEK 3: SMALL DATA STRUCTURES + OBJECT-ORIENTED PROGRAMMING
==============================================
This lesson covers small but essential Python data structures first, then dives into
Object-Oriented Programming (OOP) with practical examples, patterns, and exercises.

Topics included:
- Lists, tuples, dictionaries, sets
- Namedtuple, deque, Counter (collections)
- List/dict comprehensions and common methods
- Time/space hints and when to choose which structure

- OOP basics: classes, instances, attributes, methods
- Encapsulation, properties, class/static methods
- Inheritance and polymorphism
- Magic methods: __init__, __repr__, __str__, __eq__, __lt__
- Composition vs inheritance
- dataclasses introduction
- Simple design-pattern examples and best practices
- Exercises and homework
"""

print("🐍 Week 3: Data Structures & Object-Oriented Programming")
print("=" * 70)

# ==============================================
# PART A - SMALL DATA STRUCTURES
# ==============================================

print("\n📦 PART A — Small Data Structures")
print("-" * 40)

# LISTS
print("\n1) LISTS — ordered, mutable")
fruits = ["apple", "banana", "orange"]
print("List:", fruits)

# common operations
fruits.append("grape")
print("After append:", fruits)
fruits.insert(1, "mango")
print("After insert:", fruits)
print("Pop last:", fruits.pop())
print("Index of 'banana':", fruits.index("banana"))
print("Slice first two:", fruits[:2])

# List comprehensions
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print("Squares:", squares)

# TUPLES
print("\n2) TUPLES — ordered, immutable")
point = (10, 20)
x, y = point  # tuple unpacking
print("Point:", point, "x:", x, "y:", y)

# DICTIONARIES
print("\n3) DICTIONARIES — mapping of keys -> values")
student = {"name": "Alice", "age": 22, "grades": [85, 90, 78]}
print("Student:", student)
print("Access name:", student["name"])  # KeyError if missing
print("Get with default:", student.get("email", "no-email@example.com"))

# iterate
for key, value in student.items():
    print(f"  {key} -> {value}")

# modify
student["city"] = "Nairobi"
print("After adding city:", student)

# SETS
print("\n4) SETS — unordered, unique elements")
colors = {"red", "green", "blue"}
colors.add("yellow")
print("Colors set:", colors)
print("Is 'red' present?", "red" in colors)

# set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a-b):", a - b)

# NAMEDTUPLE and deque, Counter
print("\n5) namedtuple, deque, Counter (collections module)")
from collections import namedtuple, deque, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print("Namedtuple Point:", p, "x:", p.x)

# deque — fast append/pop from both ends
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print("Deque:", dq)

# Counter — frequency counts
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
ctr = Counter(words)
print("Counter:", ctr)
print("Most common:", ctr.most_common(2))

# WHEN TO CHOOSE WHICH
print("\nWhen to choose:")
print("- Use list for ordered collections and frequent indexing")
print("- Use tuple for fixed records or keys")
print("- Use dict for lookups by key")
print("- Use set for membership tests and removing duplicates")
print("- Use deque for queue-like operations")

# Complexity hints (very brief)
print("\nComplexity hints:")
print("- list append: O(1) amortized; insert/pop at middle: O(n)")
print("- dict/set average lookup: O(1)")
print("- tuple: like list but immutable")

# ==============================================
# PART B - OBJECT-ORIENTED PROGRAMMING (OOP)
# ==============================================

print("\n\n🏗️ PART B — Object-Oriented Programming (OOP)")
print("-" * 40)

# Basic class example
print("\n1) Basic class definition and instance")

class Person:
    """Simple Person class"""
    species = 'Homo sapiens'  # class attribute

    def __init__(self, name: str, age: int):
        self.name = name          # instance attribute
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

    def have_birthday(self):
        self.age += 1
        return self.age

p = Person("John", 30)
print(p.greet())
print("Species:", Person.species)
print("After birthday, age:", p.have_birthday())

# Encapsulation (convention)
print("\n2) Encapsulation - public vs 'protected' vs 'private' (convention)")

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._transactions = []        # intended as "protected"
        self.__balance = balance       # name-mangled (private-like)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self._transactions.append(("deposit", amount))
        return self.__balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self._transactions.append(("withdraw", amount))
        return self.__balance

    def get_balance(self):
        return self.__balance

acct = BankAccount("Alice", 100.0)
print("Balance:", acct.get_balance())
acct.deposit(50)
print("After deposit:", acct.get_balance())
try:
    acct.withdraw(500)
except ValueError as e:
    print("Withdraw error:", e)

# Class, Static methods, and Properties
print("\n3) classmethod, staticmethod, and @property")

class Circle:
    PI = 3.14159

    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self):
        return Circle.PI * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter: float):
        return cls(diameter / 2)

    @staticmethod
    def is_radius_valid(value):
        return value > 0

c = Circle(3)
print("Circle radius:", c.radius)
print("Circle area:", c.area)
print("Create from diameter:", Circle.from_diameter(10).radius)
print("Is radius valid?", Circle.is_radius_valid(-1))

# Inheritance and Polymorphism
print("\n4) Inheritance and Polymorphism")

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement speak")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

animals = [Dog("Rex"), Cat("Mittens")]
for a in animals:
    print(a.speak())  # polymorphic call

# Magic methods (dunder methods)
print("\n5) Magic methods: __repr__, __str__, __eq__, ordering")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student({self.name!r}, {self.grade!r})"

    def __str__(self):
        return f"{self.name} - {self.grade}"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.name == other.name and self.grade == other.grade

s1 = Student("Alice", 90)
s2 = Student("Alice", 90)
print(repr(s1))
print(str(s1))
print("s1 == s2?", s1 == s2)

# Comparison
print("\n6) Ordering with dunder methods (example: __lt__)")

class Box:
    def __init__(self, volume):
        self.volume = volume

    def __lt__(self, other):
        return self.volume < other.volume

boxes = [Box(10), Box(5), Box(20)]
boxes_sorted = sorted(boxes)
print("Sorted volumes:", [b.volume for b in boxes_sorted])

# Composition vs Inheritance
print("\n7) Composition vs Inheritance")

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, model, engine: Engine):
        self.model = model
        self.engine = engine

eng = Engine(150)
car = Car("Sedan", eng)
print(f"Car {car.model} with engine {car.engine.horsepower} HP")

# dataclasses (Python 3.7+)
print("\n8) dataclasses - easy boilerplate for classes")
from dataclasses import dataclass, field

@dataclass
class Product:
    id: int
    name: str
    price: float = 0.0
    tags: list = field(default_factory=list)

p = Product(1, "Laptop", 1299.99, ["electronics", "computers"]) 
print(p)

# Simple serialization (to dict)
print("Product to dict:", p.__dict__)

# Abstract Base Classes (ABC)
print("\n9) Abstract Base Classes (interface-like behavior)")
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

rect = Rectangle(3, 4)
print("Rectangle area:", rect.area())

# Best practices and SOLID (brief)
print("\n10) OOP Best Practices (short list)")
print("- Single Responsibility Principle: one class, one responsibility")
print("- Use composition over inheritance when appropriate")
print("- Keep methods small and focused")
print("- Prefer clear public APIs, hide internal details")
print("- Add unit tests for critical logic")

# ==============================================
# EXERCISES
# ==============================================

print("\n\n🧩 EXERCISES — try these in class or as homework")
print("-" * 50)

exercises = [
    "1. Create a 'Book' dataclass with title, author, year, and methods to age the book.",
    "2. Implement a 'Library' class that uses a list/dict to store books and supports add/remove/search.",
    "3. Build an 'Employee' class with subclasses Manager and Developer - each with a 'work' method.",
    "4. Implement a simple in-memory 'TaskManager' using OOP and dictionaries to map users to tasks.",
    "5. Create a 'Vector' class supporting +, -, scalar multiply, and magnitude (use dunder methods)."
]

for e in exercises:
    print(e)

# Challenge: combine data structures & OOP
print("\nChallenge: Build a small contact manager app:")
print("- Use a Contact class and a Manager class to store contacts in a dict by unique ID")
print("- Support add, update, delete, search by name, and export to CSV")

# ==============================================
# HOMEWORK
# ==============================================

homework = """
HOMEWORK — WEEK 3

1) Implement the Library class and write unit tests for add/remove/search functions.
2) Implement the Vector class with dunder methods and show vector arithmetic examples.
3) Create a small CLI using a loop that allows adding persons (using Person class) and listing them.
4) Convert the BankAccount example to use an AccountManager class that keeps multiple accounts.

Deliverables:
- Clean, commented code
- Short README describing how to run examples
- At least one unit test file using unittest or pytest
"""

print(homework)

print("\n✅ End of Week 3: Data Structures & OOP - Good luck teaching!")
print("Keep students coding and encourage explaining their design choices.")
