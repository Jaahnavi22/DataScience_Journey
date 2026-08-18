# FUNCTIONS
# A function is a reusable block of code used to perform a specific task.


# 1. FUNCTION WITHOUT ARGUMENTS

def greet():                         # Defines a function named greet
    print("Hello Python")            # Prints the message

greet()                              # Calls the function


# 2. FUNCTION WITH ARGUMENTS

def greet(name):                     # name is a parameter
    print("Hello", name)             # Prints the parameter value

greet("Jaahnavi")                    # Passes "Jaahnavi" as an argument


# 3. FUNCTION WITH MULTIPLE ARGUMENTS

def add(a, b):                       # Defines two parameters
    print(a + b)                     # Adds and prints the values

add(10, 20)                          # Passes 10 and 20 to the function


# 4. FUNCTION WITH RETURN

def add(a, b):                       # Defines the function
    return a + b                     # Returns the addition result

result = add(10, 20)                 # Stores the returned value
print(result)                        # Prints 30


# 5. DEFAULT ARGUMENT

def greet(name="User"):              # Gives a default value to name
    print("Hello", name)             # Prints the name

greet()                              # Uses the default value
greet("Jaahnavi")                    # Uses the given value


# 6. POSITIONAL ARGUMENTS

def student(name, age):              # Defines two parameters
    print(name, age)                 # Prints both values

student("Jaahnavi", 22)              # Values are passed according to position


# 7. KEYWORD ARGUMENTS

def student(name, age):              # Defines two parameters
    print(name, age)                 # Prints both values

student(age=22, name="Jaahnavi")     # Passes values using parameter names


# 8. *args

def add(*numbers):                   # Accepts multiple positional arguments
    print(sum(numbers))              # Adds all the values

add(10, 20, 30, 40)                  # Passes multiple values


# 9. **kwargs

def student(**details):              # Accepts multiple keyword arguments
    print(details)                   # Stores them as a dictionary

student(name="Jaahnavi", age=22)     # Passes keyword arguments


# 10. LAMBDA FUNCTION

square = lambda x: x ** 2             # Creates a small anonymous function

print(square(5))                     # Calls the lambda function