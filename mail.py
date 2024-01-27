# import re
# y=re.findall('[a-zA-Z0-9]+\.?[a-zA-Z0-9]*\@gmail\.com','abcd123.xyz123@gmail.com')
# print(y)


# import re
# data=re.sub('[aeiou]','@','happy republic day')
# print(data)


file=open(r"C:\Users\Administrator\Desktop\text.txt",'r')
data=file.read()
print(data)

import re
with open (r"C:\Users\Administrator\Desktop\text.txt",'r+',encoding='UTF-8')as file:
 data= file.read()
 newdata=re.sub(' ','_',data)
 file.seek(0)
 file.write(newdata)