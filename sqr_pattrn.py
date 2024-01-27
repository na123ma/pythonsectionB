a=int(input('enter the rows:- '))
temp=a//2
out=''
for i in range(a):
    for j in range(a):
        if i==temp or j==temp:
            out+='  '
        else:
            out+='+ '
    out+='\n'   
print(out)