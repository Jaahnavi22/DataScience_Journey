# ============================================================
# PYTHON COMPREHENSIONS AND REGULAR EXPRESSIONS
# ============================================================


# ============================================================
# 1. LIST COMPREHENSION
# ============================================================

# List comprehension is a short way to create a list.

numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]       # Creates squares
print(squares)                            # [1, 4, 9, 16, 25]


# List comprehension with condition

even = [x for x in numbers if x % 2 == 0] # Selects even numbers
print(even)                               # [2, 4]


# List comprehension with if-else

result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(result)                             # ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# ============================================================
# 2. SET COMPREHENSION
# ============================================================

# Set comprehension creates a set using a short syntax.

numbers = [1, 2, 2, 3, 3, 4]

squares = {x ** 2 for x in numbers}       # Creates unique squares
print(squares)                            # {1, 4, 9, 16}


# ============================================================
# 3. DICTIONARY COMPREHENSION
# ============================================================

# Dictionary comprehension creates key-value pairs.

numbers = [1, 2, 3, 4, 5]

squares = {x: x ** 2 for x in numbers}    # Creates key-value pairs
print(squares)                            # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Dictionary comprehension with condition

even = {x: x ** 2 for x in numbers if x % 2 == 0}
print(even)                               # {2: 4, 4: 16}


# ============================================================
# 4. GENERATOR COMPREHENSION
# ============================================================

# Generator comprehension produces values one at a time.

numbers = [1, 2, 3, 4, 5]

squares = (x ** 2 for x in numbers)       # Creates generator

for value in squares:
    print(value)                          # Prints squares one by one


# ============================================================
# 5. NESTED LIST COMPREHENSION
# ============================================================

# A comprehension inside another comprehension.

matrix = [[1, 2], [3, 4], [5, 6]]

result = [x for row in matrix for x in row]
print(result)                             # [1, 2, 3, 4, 5, 6]


# ============================================================
# REGULAR EXPRESSIONS (REGEX)
# ============================================================

# Regular expressions are used to search, match and
# manipulate patterns in strings.

import re


# ============================================================
# 6. re.search()
# ============================================================

# Searches for a pattern anywhere in the string.

text = "I am learning Python"

result = re.search("Python", text)

print(result)                             # Match object
print(result.group())                     # Python


# ============================================================
# 7. re.match()
# ============================================================

# Checks whether the pattern is present at the beginning.

text = "Python is easy"

result = re.match("Python", text)

print(result.group())                     # Python


# ============================================================
# 8. re.findall()
# ============================================================

# Finds all matching values and returns them as a list.

text = "Python Java Python SQL"

result = re.findall("Python", text)

print(result)                             # ['Python', 'Python']


# Find all numbers

text = "My marks are 85 and 90"

result = re.findall(r"\d+", text)

print(result)                             # ['85', '90']


# ============================================================
# 9. re.sub()
# ============================================================

# Replaces matching patterns with another value.

text = "I like Java"

result = re.sub("Java", "Python", text)

print(result)                             # I like Python


# ============================================================
# 10. re.split()
# ============================================================

# Splits the string using a regular expression.

text = "Python,Java,SQL"

result = re.split(",", text)

print(result)                             # ['Python', 'Java', 'SQL']


# ============================================================
# 11. REGEX SPECIAL CHARACTERS
# ============================================================

# \d  -> Digit (0-9)
# \D  -> Not a digit
# \w  -> Word character
# \W  -> Not a word character
# \s  -> Whitespace
# \S  -> Not whitespace
# .   -> Any character
# ^   -> Starts with
# $   -> Ends with
# +   -> One or more
# *   -> Zero or more
# ?   -> Zero or one
# []  -> Character set


# ============================================================
# 12. FIND DIGITS
# ============================================================

text = "Python 123"

result = re.findall(r"\d", text)

print(result)                             # ['1', '2', '3']


# Find complete numbers

result = re.findall(r"\d+", text)

print(result)                             # ['123']


# ============================================================
# 13. FIND WORDS
# ============================================================

text = "Python is easy"

result = re.findall(r"\w+", text)

print(result)                             # ['Python', 'is', 'easy']


# ============================================================
# 14. STARTS WITH
# ============================================================

text = "Python"

result = re.search(r"^Python", text)

print(result.group())                     # Python


# ============================================================
# 15. ENDS WITH
# ============================================================

text = "I love Python"

result = re.search(r"Python$", text)

print(result.group())                     # Python


# ============================================================
# 16. PHONE NUMBER VALIDATION
# ============================================================

phone = "9876543210"

pattern = r"^[6-9]\d{9}$"

if re.match(pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")


# ============================================================
# 17. EMAIL VALIDATION
# ============================================================

email = "example@gmail.com"

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")


# ============================================================
# 18. PASSWORD VALIDATION
# ============================================================

password = "Python@123"

# At least 8 characters
# One uppercase letter
# One lowercase letter
# One digit
# One special character

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

if re.match(pattern, password):
    print("Valid password")
else:
    print("Invalid password")


# ============================================================
# QUICK REVISION
# ============================================================

# List Comprehension       -> Creates a list
# Set Comprehension        -> Creates a set
# Dictionary Comprehension -> Creates a dictionary
# Generator Comprehension  -> Produces values one by one

# re.search()   -> Searches anywhere
# re.match()    -> Checks beginning
# re.findall()  -> Finds all matches
# re.sub()      -> Replaces matches
# re.split()    -> Splits using a pattern
