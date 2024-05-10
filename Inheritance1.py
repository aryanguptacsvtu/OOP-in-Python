class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showDetails(self):
        print(f'The name of Employee with id {self.id} is {self.name}.')


class Programmer(Employee):           # Derived Class{Programmer}
    def showLanguage(self):
        print("The defult language is Python.")
        
e1=Employee("Rohan",100)
e1.showDetails()

e2=Programmer("Harry",200)
e2.showDetails()
e2.showLanguage()
