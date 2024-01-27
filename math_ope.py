a=int(input('enter first number:- '))
b=int(input('enter second number:- '))
operator=input('enter your operator:- ')
match operator:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case '%':
        print(a%b)
    case _:
        print('invalid operator')