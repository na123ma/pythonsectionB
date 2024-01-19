print('welcome to my bus...')
dest = input('''select destination by entering
             1 for delhi
             2 for mumbai
             3 for chennai
             4 for Hydrabad:-''')
adult_seats = int(input('number of adults:- '))
child_seats = int(input('number of children:- '))
catogory = input('enter\n 1 for AC \n 2 for NON-AC \n:- ')
distance = {'1':2000,'2':800,'3':350,'4':500}
if catogory =='1':
    adult_price=10
    child_price=5
elif catogory =='2':
    adult_price=5
    child_price=3
total_price =(distance[dest]*(adult_price*adult_seats+child_price*child_seats))
print('the total amount is =',total_price,'rupees')
confirm = input('enter"YES" for confirmation or press any other key')
if confirm =='YES':
        print('your transaction successfully')
        print('thank you....\n visit again...\n Happy journey....')
else:
        print('your transaction canceld')
        print('thank you...visit again...')