def fun():
    a=1
    for i in range(1,10):
        yield i
        a=a**2
print 