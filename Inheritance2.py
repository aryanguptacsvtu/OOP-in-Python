# ** SINGLE INHERITANCE **

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal.")


class Dog(Animal):          # Derived Class {Dog}

    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed

    def make_sound(self):
        print("BARK!!") 


o1 = Animal("Dog","Mammal")
o1.make_sound()

o2 = Dog("Bruno","Doggerman")
o2.make_sound()