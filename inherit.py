# # simple inheritance

# # Base class/ parent class

# class Animal:
#     def __init__(self, name):
#         self.__name = name
    
#     def speak(self):
#         print(f"{self.__name} makes a sound.")

# # derived class

# class Dog:
#     def __init__(self):
#         self.behaviour ="friendly"

#     def speak(self):
#         print(f"{self.name} barks. he is very {self.behaviour} ")

# # Create an instance of class Animal
# animal = Animal("Generic Animal")
# animal.speak() # Output: Generic Animal makes a sound.

# # create an instance of class dog

# dog = Dog("Buddy")
# dog.speak() # Output: Buddy barks

# super keyword
# Base class
class Animal:
    def __init__(self):
        self.name ="Buddy"
    
    def speak(self):
        print (f"{self.name} makes a sound.")

# Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak() # Call the base class method
        print(f"{self.name} barks. It is a {self.breed}.")

# create an instance of Dog 

dog = Dog("Golden Retriver")
dog.speak()
# Output
# Buddy makes a sound
# Buddy barks. It is a Golden Retriver
