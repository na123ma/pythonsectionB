a1=print('bengaloore to \n 1.--->chennai \n 2.--->delhi \n 3.--->mumbai \n 4.--->hydrabad')
print('Ac Rs.10/kl\n NON AC Rs.5/kl')
a='adults'
b='childrens'
p1 =int(input('no adults:- '))
p2 = int(input('no childrens:- '))
a2=input('enter your destination location:- ')
if a==b==a2 :
    print(p1*350*10,'for adult')
    print(p2*350*5,'for children')
else:
    print(p1*350*5,'for adult')
    print(p2*350*3,'for children')
    a2=input('enter your destination location:- ')
    if a==b==a2 :
        print(p1*2000*10,'for adult')
        print(p2*2000*5,'for children')
        print('thank you visiting')
    else:
        print(p1*2000*5,'for adult')
        print(p2*2000*3,'for children')
        a2=input('enter your destination location:- ')
        if a==b==a2 :
            print(p1*800*10,'for adult')
            print(p2*800*5,'for children')
        else:
            print(p1*800*5,'for adult')
            print(p2*800*3,'for children')
            a2=input('enter your destination location:- ')
            if a==b==a2:
                print(p1*500*10,'for adult')
                print(p2*500*5,'for children')
            else:
                print(p1*500*5,'for adult')
                print(p2*500*3,'for children')