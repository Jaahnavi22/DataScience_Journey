# PYTHON OPERATORS

# 1. ARITHMETIC OPERATORS

a = 10
b = 3

print(a + b)       # 13  (Addition)
print(a - b)       # 7   (Subtraction)
print(a * b)       # 30  (Multiplication)
print(a / b)       # 3.3333333333333335  (Division)
print(a // b)      # 3   (Floor Division)
print(a % b)       # 1   (Modulus)
print(a ** b)      # 1000 (Exponentiation)


# 2. ASSIGNMENT OPERATORS

a = 10

a += 5
print(a)           # 15

a -= 3
print(a)           # 12

a *= 2
print(a)           # 24

a /= 4
print(a)           # 6.0

a //= 2
print(a)           # 3.0

a %= 2
print(a)           # 1.0

a **= 2
print(a)           # 1.0


# 3. COMPARISON OPERATORS

a = 10
b = 5

print(a == b)      # False
print(a != b)      # True
print(a > b)       # True
print(a < b)       # False
print(a >= b)      # True
print(a <= b)      # False


# 4. LOGICAL OPERATORS

a = 10
b = 5

print(a > 5 and b < 10)     # True
print(a > 15 or b < 10)     # True
print(not(a > 5))            # False


# 5. BITWISE OPERATORS

a = 5
b = 3

print(a & b)        # 1   (Bitwise AND)
print(a | b)        # 7   (Bitwise OR)
print(a ^ b)        # 6   (Bitwise XOR)
print(~a)           # -6  (Bitwise NOT)
print(a << 1)       # 10  (Left Shift)
print(a >> 1)       # 2   (Right Shift)


# 6. MEMBERSHIP OPERATORS

word = "Python"

print("P" in word)          # True
print("z" in word)          # False
print("z" not in word)      # True


# 7. IDENTITY OPERATORS

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)               # True
print(a is c)               # False
print(a is not c)           # True
