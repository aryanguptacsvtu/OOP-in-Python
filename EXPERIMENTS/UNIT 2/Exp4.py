f = open('myfile.txt','r')
text = f.read()
print(text)
f.close()

f = open('myfile.txt','w')
f.write("Hello world!!")
f.close()

f = open('myfile.txt','a')
f.write("\nAwesome!!")
f.close()

with open('myfile.txt','r') as g:
    source_content = g.read()

with open('myfile2.txt','w') as h:
    h.write(source_content)