# ** HIERARCHICAL INHERITANCE **

class A:
    def funcA(self):
        print("Welcome to class A.")

class B(A):
    def funcB(self):
        print("Welcome to class B.")

class C(A):
    def funcC(self):
        print("Welcome to class C.")

class D(B):
    def funcD(self):
        print("Welcome to class D.")


objB = B()
objB.funcB() , objB.funcA() 
print("\t")

objC = C()
objC.funcC() , objC.funcA() 
print("\t")

objD = D()
objD.funcA() , objD.funcB() , objD.funcD()
