import random
out = []
while len(out)<6:
    out+=[random.choice(['@','#','$','*','&','!'])]
    out+=[chr(random.randint(97,123))]
    out+=[str(random.randint(0,9))]
random.shuffle(out)
captcha=''
for i in out:
    captcha+=i
print(captcha)
