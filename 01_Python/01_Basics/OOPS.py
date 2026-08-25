# OBJECT ORIENTED PROGRAMMING (OOP)


# CLASS AND OBJECT

class Student:
    name = "Jaahnavi"
    age = 22


student1 = Student()

print(student1.name)
print(student1.age)


# CONSTRUCTOR

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)


student1 = Student("Jaahnavi", 22)

student1.display()


# ENCAPSULATION

class Bank:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = Bank(5000)

print(account.get_balance())


# INHERITANCE

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


dog = Dog()

dog.sound()
dog.bark()


# POLYMORPHISM

class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# ABSTRACTION

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()

dog.sound()