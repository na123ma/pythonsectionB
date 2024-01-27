b=[1,2,[4,5,6],'xyz',(4,1,2,3)]
def listtt(num):
    if type(num) in [str,tuple,list,dict,set]:
        return len(num)
    else:
        return num
print(list(map(listtt,b)))