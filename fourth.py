a=input('player 1:-')
b=input('palyer 2:-')
if a=='rock' and b=='paper':
    print('player 2 will be win')
elif a=='paper' and b=='scissor':
    print('player2 will winner')
elif a=='rock' and b=='scissor':
    print ('player 1 will win')
else:
    print('match tie')