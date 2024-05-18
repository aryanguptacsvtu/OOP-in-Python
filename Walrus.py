numbers =[1,2,3,4,5]
while (n:= len(numbers)) > 0 :
    print(numbers.pop())

print("\t")

happy = False
print(happy)
print(happy:=True)
print("\t")


foods = list()
while(x:= input("What food do you like?:")) != "quit":
    foods.append(x)
print(foods)


# "Walrus Operator" assigns values to variables as part of a larger expression.