class Rectangle:
    def __init__(self, length,width):
        self.length =length
        self.width =width
        
    def area(self):
        return self.length*self.width
    
    def perimeter(self):
        return 2*(self.length+self.width)
    
r1 = Rectangle(5,3)
r2 = Rectangle(4,6)

area1 = r1.area()  
perimeter1 = r1.perimeter()
area2 = r2.area()
perimeter2 = r2.perimeter()

print("Rectangle 1:")
print("Area:",area1)
print("Perimeter:",perimeter1)

print("\nRectangle 2:")
print("Area:",area2)
print("Perimeter:",perimeter2)