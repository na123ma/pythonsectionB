a=int(input('enter first value'))
b=int(input('enter second value'))
c=input('enter an arithametic operator')
if c=='+' :
    print (a+b)
elif c=='-':
    print (a-b)
elif c=='*':
    print (a*b)
elif c=='/':
    print (a/b)
elif c=='//':
    print (a//b)
elif c=='%':
    print (a%b)
else:
    print('invalid')