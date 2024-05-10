class MyClass:
    def __init__(self,value):
        self.value=value

    def show(self):
        print(f'Value is {self.value}')
    
    @property                  # GETTER
    def ten_value(self):
        return 10*self.value

    @ten_value.setter          # SETTER
    def ten_value(self,new_value):
        self.value=new_value/10


obj=MyClass(10)
obj.ten_value=67
print(obj.ten_value)
obj.show()

# "Getters" are used to return the value of an object's properties.They don't take any parameters.
# "Setters" are used to set the value.