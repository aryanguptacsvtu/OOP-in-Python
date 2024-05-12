l1=[12,34,22,54,65,78,97,5,0,55]
print("Length of list:",len(l1))
print('\t')

print("Indexing Operations:")
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[8])
print('\t')

print("Slicing a list:-")
print(l1[:])
print(l1[0:])
print(l1[:len(l1)])
print(l1[4:8])
print(l1[:-4])
print(l1[-8:-4])
print('\t')

print("List Concatenation:-")
l2=['apple','mango',55]
l3=l1+l2
print(l3)
print('\t')

print("List Repetition:-")
print(l1*2)
print(l2*3)