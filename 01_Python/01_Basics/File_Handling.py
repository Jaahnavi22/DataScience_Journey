# FILE HANDLING
# File handling is used to create, read, write, append and manage files.


# 1. WRITE TO A FILE
# "w" mode creates a new file or overwrites an existing file.

file = open("sample.txt", "w")
file.write("Hello Python")
file.close()


# 2. READ A FILE
# "r" mode is used to read the contents of a file.

file = open("sample.txt", "r")
data = file.read()
print(data)
file.close()


# 3. READ ONE LINE
# readline() reads one line from the file.

file = open("sample.txt", "r")
print(file.readline())
file.close()


# 4. READ ALL LINES
# readlines() returns all lines as a list.

file = open("sample.txt", "r")
print(file.readlines())
file.close()


# 5. APPEND TO A FILE
# "a" mode adds new content at the end without deleting existing content.

file = open("sample.txt", "a")
file.write("\nWelcome to Python")
file.close()


# 6. USING WITH STATEMENT
# "with" automatically closes the file after the operation.

with open("sample.txt", "r") as file:
    data = file.read()
    print(data)


# 7. WRITE MULTIPLE LINES
# writelines() writes multiple strings into a file.

lines = ["Python\n", "Java\n", "C++\n"]

with open("languages.txt", "w") as file:
    file.writelines(lines)


# 8. CHECK FILE POSITION
# tell() returns the current position of the file cursor.

with open("sample.txt", "r") as file:
    print(file.tell())


# 9. CHANGE FILE POSITION
# seek() moves the file cursor to a specific position.

with open("sample.txt", "r") as file:
    file.seek(0)
    print(file.read())


# 10. FILE EXISTS CHECK
# os.path.exists() checks whether a file exists.

import os

print(os.path.exists("sample.txt"))


# 11. DELETE A FILE
# os.remove() deletes the specified file.

# os.remove("sample.txt")


# FILE MODES
# "r"  → Read
# "w"  → Write
# "a"  → Append
# "x"  → Create a new file
# "r+" → Read and write
# "w+" → Write and read
# "a+" → Append and read