class Circle:
    def __init__(self,radius):
        self.__radius = radius

    def print_radius(self):
        return self.__radius
    
    def set_radius(self,radius):
        self.__radius = radius

    def area(self):
        return 3.14*self.__radius**2
    
circle = Circle(5)

print("Radius:",circle.print_radius())
print("Area:",circle.area())

circle.set_radius(10)
print("New Radius:",circle.print_radius())
print("New Area:",circle.area())