price = int(input("Enter the price:"))
if(price>100):
    print("Price is greater than 100.")
elif(price==100):
    print("Price is 100.")
elif(price<100):
    print("Price is less than 100.")
print('\t')


rows = int(input("Enter the rows:"))
for i in range(0,rows+1):
    for j in range(i):
        print(i , end =" ")
    print(' ')


print('\t')
lang = ['Java','Python','C++']
for x in lang:
    if (x=='Python'):
        break
    print(x)