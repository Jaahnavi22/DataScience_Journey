# PYTHON INPUT AND OUTPUT

# OUTPUT

print("Hello World")              # Displays Hello World
print(10)                         # Displays 10
print("Python", "Programming")    # Python Programming


# INPUT

name = input("Enter your name: ")
print(name)

age = input("Enter your age: ")
print(age)


# INPUT WITH DIFFERENT DATATYPES

age = int(input("Enter your age: "))
print(age)

marks = float(input("Enter your marks: "))
print(marks)


# MULTIPLE INPUTS

a, b = input("Enter two values: ").split()
print(a)
print(b)


# MULTIPLE INTEGER INPUTS

a, b = map(int, input("Enter two numbers: ").split())
print(a)
print(b)


# OUTPUT USING SEPARATOR

print("Python", "Java", "C++", sep=" | ")
# Python | Java | C++


# OUTPUT USING END

print("Hello", end=" ")
print("World")
# Hello World


# FORMATTED OUTPUT

name = "Jaahnavi"
age = 22

print(f"My name is {name} and I am {age} years old.")
# My name is Jaahnavi and I am 22 years old.