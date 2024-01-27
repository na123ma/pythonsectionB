import re
a=re.findall('[^0-9]','abcdef12gh45')
print(a)

import re
a=re.findall('$','abcdef12gh45')
print(a)

import re
a=re.findall('[0-9]','ab8def123gh45@$')
print(a)


import re
data=re.findall('[0,9]{1,3}','abcd8iweh30u3jd99')
print(data)