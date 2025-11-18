board = {'tl':'   ','tm':'   ','tr':'   ',
         'ml':'   ','mm':'   ','mr':'   ',
         'll':'   ','lm':'   ','lr':'   '}
print("Lets play tic tac toe \nThe base:")
print('tl'+'|'+'tm'+'|'+'tr')
print('--+--+--')
print('ml'+'|'+'mm'+'|'+'mr')
print('--+--+--')
print('ll'+'|'+'lm'+'|'+'lr')

def printboard(board):
    print(board['tl']+'|'+board['tm']+'|'+board['tr'])
    print('---+---+---')
    print(board['ml']+'|'+board['mm']+'|'+board['mr'])
    print('---+---+---')
    print(board['ll']+'|'+board['lm']+'|'+board['lr'])

def check(board):
    if ((board['tl']== board['tm']==board['tr']!='   ') or (board['tl']== board['mm']==board['lr']!='   ') or
       (board['ll']== board['mm']==board['tr']!='   ') or (board['ml']==board['mm']==board['mr']!='   ')or
       (board['ll']==board['lm']==board['lr']!='   ') or (board['tl']==board['ml']==board['ll']!='   ') or
        (board['tm']==board['mm']==board['lm']!='   ') or (board['tr']==board['mr']==board['lr']!='   ')):
        return True


turn ='X'
i=1
while True:
    print("What type of game u wanna play duo or with bot?\nPlease type 'duo' or 'bot'")
    typ=input()
    if typ=='duo' or typ=='bot':
        print("\nLet's start the game:\n")
        break
    else:
        print("\nPlease senpai don't be messy\n")

    
import random
choose=['tl','tm','tr',
        'ml','mm','mr',
        'll','lm','lr']

while True:
    printboard(board)
    if (typ=='bot' and turn=='0'):
        x=random.choice(choose)
        print(x)
        move=x
    else:
        print('Turn for '+turn+' move '+str(i)+' in which space?')
        move=input()
    
        
    if move not in choose:
        print("Invalid input\nTry again:")
        continue
    else:
        board[move]=' '+turn+' '
        del choose[choose.index(move)]
    i+=1
        
    if turn=='X':
        if check(board):
            if typ=='bot':
                turn='You'
            print('\n\nWow '+turn +' win the match\n\n')
            break
        else:
            turn='0'
    else:
        if check(board):
            if typ=='bot':
                turn='bot'
            print('\n\nWow '+turn +' win the match\n\n')
            break
        else:
            turn='X'
        

printboard(board)
