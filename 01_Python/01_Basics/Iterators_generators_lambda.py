# ITERATORS, GENERATORS, LAMBDA, NESTED FUNCTIONS AND DECORATORS


# ============================================================
# 1. ITERATORS
# ============================================================

# An iterator is used to access elements one by one.
# iter() creates an iterator and next() gets the next value.

numbers = [10, 20, 30, 40]

iterator = iter(numbers)               # Creates an iterator

print(next(iterator))                  # 10
print(next(iterator))                  # 20
print(next(iterator))                  # 30
print(next(iterator))                  # 40


# Iterator using for loop

numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)               # Creates an iterator

for value in iterator:                 # Gets values one by one
    print(value)                       # Displays each value


# ============================================================
# 2. GENERATORS
# ============================================================

# A generator produces values one at a time.
# yield is used to produce values from a generator function.

def numbers():
    yield 1                            # Produces 1
    yield 2                            # Produces 2
    yield 3                            # Produces 3


result = numbers()                     # Creates generator object

print(next(result))                    # 1
print(next(result))                    # 2
print(next(result))                    # 3


# Generator using for loop

def count_numbers():
    for i in range(1, 6):              # Loops from 1 to 5
        yield i                        # Produces one value at a time


for number in count_numbers():
    print(number)                      # Displays each value


# Generator for squares

def squares(n):
    for i in range(1, n + 1):          # Loops from 1 to n
        yield i ** 2                   # Produces square


for value in squares(5):
    print(value)                       # Displays squares


# ============================================================
# 3. LAMBDA FUNCTIONS
# ============================================================

# Lambda is a small anonymous function.
# It contains a single expression.


# Simple lambda

square = lambda x: x ** 2              # Creates square function

print(square(5))                       # 25


# Lambda with multiple arguments

add = lambda a, b: a + b               # Adds two values

print(add(10, 20))                     # 30


# Lambda with condition

check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))                       # Even
print(check(7))                        # Odd


# Lambda with map()

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))
# Applies lambda to every element

print(squares)                         # [1, 4, 9, 16, 25]


# Lambda with filter()

numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))
# Selects only even numbers

print(even)                            # [2, 4, 6]


# ============================================================
# 4. NESTED FUNCTIONS
# ============================================================

# A function defined inside another function is called
# a nested function.


# Simple nested function

def outer():

    def inner():                       # Inner function
        print("This is inner function")

    inner()                            # Calls inner function


outer()                                # Calls outer function


# Nested function with parameters

def outer(a):

    def inner(b):                      # Inner function
        return a + b                   # Uses outer function value

    return inner(10)                   # Calls inner function


print(outer(20))                       # 30


# Function returning another function

def outer():

    def inner():
        print("Hello Python")

    return inner                       # Returns inner function


result = outer()                       # Stores returned function
result()                               # Calls inner function


# ============================================================
# 5. DECORATORS
# ============================================================

# A decorator modifies or extends the behavior of a function
# without changing its original code.


# Simple decorator

def decorator(func):                   # Receives original function

    def wrapper():                     # Wrapper function
        print("Before function")       # Executes before function
        func()                         # Calls original function
        print("After function")        # Executes after function

    return wrapper                     # Returns wrapper


@decorator                             # Applies decorator
def greet():
    print("Hello Python")


greet()                                # Calls decorated function


# Decorator with arguments

def decorator(func):

    def wrapper(name):                 # Accepts function argument
        print("Welcome")               # Executes before function
        func(name)                     # Calls original function

    return wrapper


@decorator
def greet(name):
    print("Hello", name)


greet("Jaahnavi")


# Decorator with *args and **kwargs

def decorator(func):

    def wrapper(*args, **kwargs):      # Accepts any arguments
        print("Function started")      # Executes before function

        result = func(*args, **kwargs) # Calls original function

        print("Function completed")    # Executes after function

        return result                  # Returns function result

    return wrapper


@decorator
def add(a, b):
    return a + b                       # Returns addition


print(add(10, 20))                     # 30


# ============================================================
# QUICK REVISION
# ============================================================

# Iterator   → Accesses values one by one using iter() and next()
# Generator  → Produces values one at a time using yield
# Lambda     → Small anonymous function
# Nested     → Function inside another function
# Decorator  → Adds functionality to an existing function
