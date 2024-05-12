class Math:
    def __init__(self,num):
        self.num =num

    def addToNum(self,n):
        self.num = self.num + n

    @staticmethod
    def Add(a,b):   # No need to pass "self".
        return a+b
    
a=Math(10)
print("Initial:",a.num)
a.addToNum(15)
print("After sum:",a.num)

print("Using Static Method:-")
print(a.Add(5,8))
print(Math.Add(6,6))

# 'Static Methods' are methods that belong to a class rather than an instance of the class.