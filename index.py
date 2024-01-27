def fname(arr):
    out=[]
    for i in arr:
        if type(i) in [str,list,tuple,set,dict]:
            for j in i:
                out+=[j]
    return out