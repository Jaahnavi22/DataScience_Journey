# PACKAGES

# Importing a module from a package
from mypackage import calculator

print(calculator.add(10, 20))


# Importing a specific function from a package
from mypackage.calculator import add

print(add(10, 20))


# Importing a module with an alias
import mypackage.calculator as calc

print(calc.add(10, 20))       # Calls add() using the alias