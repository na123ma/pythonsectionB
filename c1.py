st=input('enter your string')
i=0
out=[]
start=0
while i<len(st):
    if st[i]=='':
         out+=[st[start:i]]
         start=i+1
    i+=1
if start<i:
    out+=[st[start:]]
print(out)