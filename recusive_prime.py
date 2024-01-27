
def func(a,i=2):
        if a%i==0:
            print('not a prime')
        else:
            print(' prime')
        return func
print(func(7))