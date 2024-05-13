class Parent:
    def parent_method(self):
        print("This is the parent method 1.")

class Child(Parent):
    def parent_method(self):
        print("HARRY")
        super().parent_method()

    def child_method(self):
        print("This is the child method.")
        super().parent_method()


child_obj= Child()
child_obj.child_method()
print("\t")
child_obj.parent_method()

# The "super()" keyword is used to refer to the parent class. 
# It can be employed to use the parent class method in child class.