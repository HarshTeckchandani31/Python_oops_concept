# simple inheritance

# Base class/ parent class

class Animal:
    def __init__(self, name):
        self.__name = name
    
    def speak(self):
        print(f"{self.__name} makes a sound.")

# derived class

class Dog:
    def __init__(self):
        self.behaviour ="friendly"

    def speak(self):
        print(f"buddy barks. he is very {self.behaviour} ")

# Create an instance of class Animal
# animal = Animal("Generic Animal")
# animal.speak() # Output: Generic Animal makes a sound.

# create an instance of class dog

dog = Dog()
dog.speak() # Output: Buddy barks