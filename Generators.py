def my_generator():
    for i in range(8):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print("\t")

for j in gen:
    print(j)


'''
"Generators" allow you to generate the values one-by-one as you iterate over it , rather than having to create & store the entire sequence in memory.

The "yield" statement returns a value from the generator & suspends the execution of function until the next value is requested. 
The "next()" function is used to request the next value from the generator.

'''