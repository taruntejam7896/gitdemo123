from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass  # Abstract method with no implementation

    def sleep(self):
        print("This animal is sleeping.")

# Subclass 1
class Dog(Animal):
    def sound(self):
        print("Dog says: Woof!")

# Subclass 2
class Cat(Animal):
    def sound(self):
        print("Cat says: Meow!")

# Using the classes
d = Dog()
d.sound()
d.sleep()

c = Cat()
c.sound()
c.sleep()
