class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x *self.y
    

class Circle(Shape):           # Derived Class
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14* self.radius * self.radius 


obj1 = Shape(10,3)
print(obj1.area())

obj2 = Circle(10)
print(obj2.area())