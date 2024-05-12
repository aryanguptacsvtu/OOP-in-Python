tup=(1,32,43,4,'hello',55,80,'dog',12,'lion')
print("Length of Tuple:",len(tup))
print('\t')

print("Indexing Operations:")
print(tup[0])
print(tup[1])
print(tup[4])
print(tup[5])
print("\t")

print("Slicing a Tuple:")
print(tup[:])
print(tup[3:7])
print(tup[-7:-2])
print(tup[::2])
print(tup[2:9:3]) 
print("\t")

A=("Pakistan","India","Bangladesh")
print("Tuple Concatenation:")
B=A+tup                   
print(B)
print("\t")

print("Tuple Repetition:")
print(A*2)

