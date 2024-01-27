def fun(a,out=1):
    if a==1:
        return out
    out*=a
    return fun(a-1,out)
print(fun(5))