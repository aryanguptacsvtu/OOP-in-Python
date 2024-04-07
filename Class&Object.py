# "Class" is a blueprint/template for creating Objects.

class Person:
    name="Harry"
    occupation="Software Developer"

    def info(self):
        print(f"{self.name} is a {self.occupation}.")


a=Person()     # Objects[a,b,c]
b=Person()
c=Person()

a.info()

b.name='Arun'
b.occupation="Doctor"
print(b.name,b.occupation)

c.info()      # Here,'c' gets default values. 

b.name ="Aryan"
b.occupation="Engineer"
b.info()


# The "self" parameter is a reference to the current instance of the class.
# It is used to access variables that belongs to the class. 
# It must be provided as extra parameter inside the method definition.
