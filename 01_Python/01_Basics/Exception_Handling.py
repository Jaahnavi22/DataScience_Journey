# EXCEPTION HANDLING

# try and except
try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")


# ValueError
try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Please enter a valid number")


# Multiple exceptions
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")


# else
try:
    a = 10
    b = 2
    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print(result)


# finally
try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("Program completed")


# raise
age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")