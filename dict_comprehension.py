 #def fun():
a=[4,9,'abc',[1,2,3,4]]
    #b={i:a[i] for i in range(len(a))}
   # print(b)
#fun()
out={i:j for i,j in enumerate(a)}
print(out)