# ** MULTILEVEL INHERITANCE **

class Animal:
    def __init__(self, name,species):
        self.name =name
        self.species =species

    def show(self):
        print(f'Name:-{self.name}')
        print(f'Species:-{self.species}')


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species='Dog')
        self.breed =breed

    def show(self):
        Animal.show(self)
        print(f'Breed:-{self.breed}')


class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self,name,breed='GoldenRetriever')
        self.color =color

    def show(self):
        Dog.show(self)
        print(f'Color:-{self.color}')


o = GoldenRetriever("Tommy","Black")
o.show()
print(GoldenRetriever.mro())
print("\t")

a = Dog('Bruno','Husky')
a.show()
print("\t")

b = Animal('Billy','Dog')
b.show()
