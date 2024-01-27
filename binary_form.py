def func(num):
    if type(num) in [int]:
        yield bin(num)
    else:
        yield num
out=func(10)
print(list(out))



def binary(num):
    while num>0:
        yield num%2
        num = num//2
out=''
for i in binary(100):
    out=str(i)+out
print(out)