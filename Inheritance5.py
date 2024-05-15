# ** HYBRID INHERITANCE **

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:-",self.name)
        print("Age:-",self.age)


class Person(Human):
    def __init__(self,name,age,address):
        Human.__init__(self,name,age)
        self.address = address

    def show(self):
        Human.show(self)
        print("Address:-",self.address)


class Program:
    def __init__(self,programName,duration):
        self.programName = programName
        self.duration = duration

    def show(self):
        print("Program Name:-",self.programName)
        print("Duration:-",self.duration)


class Student(Person):
    def __init__(self, name, age, address,program):
        Person.__init__(self,name, age, address)
        self.program=program

    def show(self):
        Person.show(self)
        self.program.show()


obj1 =Program("Computer Science",4)
obj2 = Student("John",25,"Sector-17",obj1)

obj2.show()
print("\t")
obj1.show()