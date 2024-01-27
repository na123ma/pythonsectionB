b=int(input('enter no of rows:- '))
temp=b//2
out=''
for i in range(b):
    for j in range(b):
        if i in [j,b-j-1,temp] or j in [temp]:
           out+='* '
        else:
            out+='  '
    out+='\n'
print(out)