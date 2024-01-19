s=input('')
out ={}
for char in s:
    if not char in out:
        out[char]=1
    else:
        out[char]+=1
print(out)