def  even(value):
    flag=False
    if value%2==0:
        flag=True
    return flag
def SquAdd(a,b):
    return a**2+b**2
def add(a,b):
    return a+b
def index_value(arr):
    out=[]
    for i in range(len(arr)):
        if not (even(i)^even(arr[i])):
            out+=[SquAdd(i,arr[i])]
        else:
            out+=[add(i,arr[i])]
    return out
print(index_value([1,2,3,4,5,3,6,2,7,1,9]))