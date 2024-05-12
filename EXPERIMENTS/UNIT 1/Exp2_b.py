a="Hello world!!"
b="CSVTU"

print("Length of string a:",len(a))
print("Length of string b:",len(b))
print('\t')

print("String Indexing:-")
print(a[0])
print(a[7])
for i in range(len(b)):
    print(b[i])
print('\t')

print("String Slicing:-")
print(a[:])
print(a[2:8])
print(a[:-6])
print(a[-5:-2])
print(b[::2])
print('\t')

print("String Concatenation:",a+b)
print("String Repetition:",a*2)
