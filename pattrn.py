s=int(input('enter no of rows:- '))
out=''
for i in range(s):
    for j in range(s):
        if i==j or i == s-j-1:
           out+='  '
        else:
           out+='*  '
    out+='\n'
name = input('enter file name:-  ')
with open (f'{name}.txt','w')as file:
    file.write(out)