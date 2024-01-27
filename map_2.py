a=[2,8,6,4,3,23,2,1,8,9]
def cube(num):
    if num%2==0:
        return num**3
    else:
        return num
print(list(map(cube,a)))
print(list(map(lambda k:k**3,filter(lambda i:i%2==0,a))))