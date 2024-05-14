class Employee:
    def __init__(self,name):
        self.name=name

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    
    def __str__(self):
        return f'The name of the Employee is {self.name}.'

    def __repr__(self):
        return f'The Employee is {self.name}.'

    def __call__(self):
        print("GOOD MORNING!!")


e=Employee('Harry')
print(e.name)
print(len(e))

print(str(e))
print(repr(e))
print("\t")

print(e)
print("\t")

e()  #{Possible due to call method}  


# Magic Methods("dunders") allow you to customize the behaviour of classes.

# "__init__" method is automatically invoked when you create a new instance of a class.

# "__str__" method is used when you want to print out an object.
# "__repr__" method is used to get a string representation of an object that can be used to recreate the object.

# "__len__" method is used to get length of an object.

# "__call__" method is used to make an object callable.