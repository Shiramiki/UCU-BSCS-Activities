class  MyClass:
    pass

object1 = MyClass()
object2 = MyClass()

print(object1)
print(object2)
print(type(object1))
print(type(object2))

"""
    Classes are used to create data types. This where we get Object oriented programing
    A class is user defined datatype or a blueprint of a datatype

    An object is an instance of a class
    def __init__(self):
        creates objects 

    All Functions in a class are called a method. 
    in a class we either find methods or variables/ datatypes or tools

    danda function- is a function with double underscore. 
    create a instance of a class (to instantiate)
    
"""

def __init__(self):
    self.colour = "green"
    self.fruit = "orange"

fruit1 = MyClass()
print(fruit1.colour)
print(fruit1.fruit)

