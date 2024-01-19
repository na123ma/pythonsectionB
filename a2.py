a=float(input('enter student score:-'))
if a<90 and a>=100:
    print('student got A+ grade')
elif a<=90 and a>80:
    print('student got A grade')
elif a <=80 and a>70:
    print ('student got B+ grade')
elif a<=70 and a>60:
    print('student got B grade')
elif a<=60 and a>50:
    print ('student got c grade')
elif a<=50 and a>=35:
    print('student got pass marks ')
elif a <35:
    print ('student is FAIL')
else:
    print('invalid grade')