class random:

    def __init__(self):        # Default Constructor.
        print("Hello!")

X =random()


class Person:
        
    def __init__(self,n,o):    # Parameterized Constructor.
        self.name=n
        self.occ=o


    def info(self):
        print(f"{self.name} is a {self.occ}.")


a=Person("Harry","Developer")
b=Person("Tom","HR")
# c=Person() {INVALID}
# d=Person("A","b","g") {INVALID}
a.info()
b.info()


# A 'Constructor' is a unique function that gets called automatically when an Object is created.It can't return any value other than None.

# "Default Constructor":- When constr. doesn't accept any arguments from object & has only 'self' .
# "Parameterized Constructor":- When constr. accepts arguments along with self.