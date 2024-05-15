# ** MULTIPLE INHERITANCE **

class Employee:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f'The name is {self.name}.')

class Dancer:
    def __init__(self,dance):
        self.dance = dance

    def show(self):
        print(f'The dance is {self.dance}.')


class Derived(Dancer,Employee):
    def __init__(self, dance,name):
        self.dance = dance
        self.name = name


obj = Derived("Kathak","Shivani")
print(obj.name)
print(obj.dance)

obj.show()
print(Derived.mro())
print("\t")

x = Dancer("Hiphop")
print(x.dance)
x.show()

# The "Method Resolution Order"(MRO) determine the order in which parent classes are searched for attributes & methods.
