class Employee:
    company = "Apple"
    
    def show(self):
        print(f'The name is {self.name} and company name is {self.company}.')

    @classmethod
    def changeCompany(cls , newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)


# "Class Methods" are used to define functions that operate on the class as a whole,rather than on a specific instance of class.