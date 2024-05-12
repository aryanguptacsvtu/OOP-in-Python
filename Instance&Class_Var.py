class Employee:
    companyName="Apple"
    noOfEmployees=0    # Class Variables 

    def __init__(self,name):
        self.name=name
        self.raise_amount = 5       # Instance Variables
        Employee.noOfEmployees += 1

    def showDetails(self):
        print(f'The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}.')
        

emp1 = Employee("Harry")
emp1.raise_amount = 7
emp1.companyName = 'Microsoft'
emp1.showDetails()

emp2 = Employee("Rohan")
emp2.showDetails()

Employee.companyName="Netflix"
print(Employee.companyName)

emp3 =Employee("Arun")
emp3.showDetails()

# "Class Variables" are defined at the class level and are shared among all instances of the class.
# They are defined outside of any methods.

# "Instance Variables" are defined at the instance level and are unique to each instance of the class.
# They are defined inside the __init__ method.