class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0] , int(string.split("-")[1]))
        
e1 = Employee("Harry" , 12000)
print(e1.name)
print(e1.salary)

string= "John-15000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)
print('\t')


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name,age = string.split(',')
        return cls(name , int(age))
    
obj = Person.from_string("Chris,30")
print(obj.name)
print(obj.age)
