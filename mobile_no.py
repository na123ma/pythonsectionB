class MobileNumberError(Exception):
    pass
try:
    mobile=(input('enter your mobile number:- '))
    if len(mobile)<10:
        raise MobileNumberError(f'mobile number should be more than 10 numbers but {len(mobile)} we are given')
    else:
       print('mobile number validated')
except(MobileNumberError) as e:
    print(e)