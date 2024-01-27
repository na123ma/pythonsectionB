a=10
try:
    a+'10'
except TypeError:
    print('exception handled')
b=40
c=50
print(a+b+c)