def index(str):
       i=0
       out=[]
       while i<len(str):
              if  str[i] in 'aeiouAEIOU':
                     out+=[i]
              i+=1
       return out
print(index('how are you'))