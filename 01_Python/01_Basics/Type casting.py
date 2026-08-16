# TYPE CASTING

# 1. INTEGER TO FLOAT

a = 10
b = float(a)

print(b)              # 10.0
print(type(b))        # <class 'float'>


# 2. FLOAT TO INTEGER

a = 10.5
b = int(a)

print(b)              # 10
print(type(b))        # <class 'int'>


# 3. INTEGER TO STRING

a = 100
b = str(a)

print(b)              # 100
print(type(b))        # <class 'str'>


# 4. STRING TO INTEGER

a = "100"
b = int(a)

print(b)              # 100
print(type(b))        # <class 'int'>


# 5. STRING TO FLOAT

a = "10.5"
b = float(a)

print(b)              # 10.5
print(type(b))        # <class 'float'>


# 6. FLOAT TO STRING

a = 10.5
b = str(a)

print(b)              # 10.5
print(type(b))        # <class 'str'>


# 7. INTEGER TO BOOLEAN

a = 1
b = bool(a)

print(b)              # True
print(type(b))        # <class 'bool'>


# 8. STRING TO BOOLEAN

a = ""
b = bool(a)

print(b)              # False
print(type(b))        # <class 'bool'>


# 9. LIST TO TUPLE

a = [1, 2, 3]
b = tuple(a)

print(b)              # (1, 2, 3)
print(type(b))        # <class 'tuple'>


# 10. TUPLE TO LIST

a = (1, 2, 3)
b = list(a)

print(b)              # [1, 2, 3]
print(type(b))        # <class 'list'>


# 11. LIST TO SET

a = [1, 2, 2, 3]
b = set(a)

print(b)              # {1, 2, 3}
print(type(b))        # <class 'set'>