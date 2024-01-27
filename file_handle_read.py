file = open('sample.txt','w')
data='Happy Republic day'
file.write(data)
file.close()


file=open(r"C:\Users\Administrator\Desktop\New Text Document.txt",'r')
data = file.read()
print(data)

file = open('sample.txt','a')
data=' suresh'
file.write(data)
file.close()
