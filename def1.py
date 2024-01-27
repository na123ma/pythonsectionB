class nareshError(Exception):
    pass

name=input('enter your name:- ')
if len(name)<=4:
    raise nareshError(f'name should be more than 4 charecters but {len(name)} we are given')
else:
    print('name is validate')