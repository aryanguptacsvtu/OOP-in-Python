x=[1,2,3]
print(dir(x))
print(x.__add__)
print(x.clear)
print("\n")

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("aryan",18)
print(p.__dict__)
print("\n")

print(help(Person))
print(help(list))

# The "dir()" function returns a list of all the attributes and the methods available for an object.

# The "__dict__" attribute returns a dictionary representation of an object's attributes.

# The "help()" function is used to get help documentation for an object,including a description of its attributes and methods.
