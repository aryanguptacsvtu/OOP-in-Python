class Employee:
    def __init__(self):
        self.__name="Harry"     # "Private" 

a=Employee()
# print(a.__name)  {Cannot be accessed directly}

print(a._Employee__name)  # {Can be accessed indirectly}
# Using "Name Mangling"
print('\t')


class Student:
    def __init__(self):
        self._x="Rohan"

    def _funcName(self):      # "Protected"
        return "Coding In Python!!"
    
class Subject(Student):      # Inherited Class
    pass
    
obj1=Student()
obj2=Subject()

print(obj1._x)
print(obj1._funcName())

print(obj2._x)
print(obj2._funcName())


# "Name Mangling" is a technique uesd to protect 'Private' attributes from being accidently overwritten by subclasses.
# It is done by the addition of a single leading underscore and a double leading underscore respectively.