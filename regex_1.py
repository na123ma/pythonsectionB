import re
a=re.findall('[6-9][0-9]{9}','+91 9126419464')
print(a)


import re
c=re.findall('[A-Z]{5}[0-9]{4}[A-Z]','ABCDE1234F')
print(c)

import re 
d=re.findall('[a-zA-Z]{2}[][0-9]{2}[][A-Z][][0-9]{4}','Ap01A1234')
print(d)


import re 
x=re.findall('Ap[]?[0-3][1-9][]?[a-zA-Z][]?[0-9]{4}','Ap01A1234')
print(x)