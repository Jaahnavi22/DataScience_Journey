word="Python"       #string
#   BUILT-IN-FUNCTIONS OF STRING(THEY ARRANGE BASED ON THE ASCII VALUES)
print(len(word))            #6
print(max(word))            #y
print(min(word))            #p
print(sorted(word))         #['P', 'h', 'n', 'o', 't', 'y']

#   STRING METHODS
print(word.upper())         #PYTHON
print(word.lower())         #python
print(word.capitalize())    #Python  (capitalize the first letter of sentence.)
print(word.title())         #Python  (capitalize every word in the sentence )
print(word.casefold())      #python  (aggressively converts into lowercase)
print(word.swapcase())      #pYTHON  (converts the lower case into upper case and vice_versa.)


# SEARCHING METHODS
word = "Python Programming"
print(word.find("P"))        #0   (returns first occurrence index, -1 if not found)
print(word.rfind("m"))       #17  (returns last occurrence index)
print(word.index("P"))       #0   (same as find(), but gives error if not found)
print(word.rindex("m"))      #17  (same as rfind(), but gives error if not found)

# COUNTING METHOD

print(word.count("m"))       #2   (counts the number of occurrences)

# CHECKING METHODS

print(word.startswith("Py"))     #True   (checks if string starts with given value)
print(word.endswith("ing"))      #True   (checks if string ends with given value)
print(word.isalpha())            #False  (contains only alphabets)
print(word.isdigit())            #False  (contains only digits)
print(word.isalnum())            #False  (contains only alphabets and numbers)
print(word.isspace())            #False  (contains only spaces)
print(word.islower())            #False  (checks if all characters are lowercase)
print(word.isupper())            #False  (checks if all characters are uppercase)
print(word.istitle())            #True   (checks if every word starts with uppercase)
print(word.isascii())            #True   (checks if all characters are ASCII)

# MODIFICATION METHODS

print(word.replace("Python", "Java"))       #Java Programming
print(word.strip())                                  #Python Programming   (removes spaces from both sides)
print(word.lstrip())                                 #Python Programming   (removes spaces from left side)
print(word.rstrip())                                 #Python Programming   (removes spaces from right side)
print(word.center(25, "*"))             #****Python Programming****
print(word.ljust(25, "-"))              #Python Programming------
print(word.rjust(25, "-"))              #------Python Programming
print(word.zfill(25))                                #000000Python Programming


word = "Python"

# ENCODING AND DECODING METHODS

encoded = word.encode()          #Converts string into bytes (UTF-8 by default)
print(encoded)                   #b'Python'

decoded = encoded.decode()       #Converts bytes back into string
print(decoded)                   #Python
