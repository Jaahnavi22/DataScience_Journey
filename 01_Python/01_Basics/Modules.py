# MODULES
# A module is a Python file containing reusable code such as functions and variables.


# 1. IMPORT A MODULE

import math                           # Imports the built-in math module

print(math.sqrt(25))                  # Finds the square root of 25


# 2. IMPORT A SPECIFIC FUNCTION

from math import sqrt                  # Imports only the sqrt function

print(sqrt(25))                       # Calls sqrt directly


# 3. IMPORT MULTIPLE FUNCTIONS

from math import sqrt, factorial       # Imports two functions from math

print(sqrt(16))                       # Finds square root
print(factorial(5))                   # Finds factorial


# 4. MODULE ALIAS

import math as m                       # Gives math a shorter name

print(m.sqrt(25))                     # Uses the alias to call sqrt


# 5. FUNCTION ALIAS

from math import factorial as fact     # Gives factorial a shorter name

print(fact(5))                        # Calls factorial using the alias


# 6. RANDOM MODULE

import random                          # Imports the random module

print(random.randint(1, 10))          # Generates a random number from 1 to 10


# 7. DATETIME MODULE

import datetime                        # Imports the datetime module

today = datetime.date.today()         # Gets today's date
print(today)                          # Displays today's date


# 8. OS MODULE

import os                              # Imports the operating system module

print(os.getcwd())                    # Displays the current working directory


# 9. DIR() FUNCTION

import math                            # Imports the math module

print(dir(math))                      # Displays available names in math module