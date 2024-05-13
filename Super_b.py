class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self,name,id,lang):

        super().__init__(name,id)
        self.lang = lang


a=Employee("Rohan",420)
b=Programmer("Harry",1000,"Python")

print(a.name)

print(b.name)
print(b.id)
print(b.lang)