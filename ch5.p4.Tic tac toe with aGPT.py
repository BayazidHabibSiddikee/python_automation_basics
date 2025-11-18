import random
board={
    'tl':'   ','tm':'   ','tr':'   ',
    'ml':'   ','mm':'   ','mr':'   ',
    'll':'   ','lm':'   ','lr':'   '}

print("Let's play tik tak toe!\nHere are the positions:")
print("tl | tm | tr"+ "\n---+----+---" + "\nml | mm | mr\n---+----+---\nll | lm | lr\n")

def pboard(board):
    print(board['tl'] + '|' + board['tm'] + '|' + board['tr'])
    print('---+---+---')
    print(board['ml'] + '|' + board['mm'] + '|' + board['mr'])
    print('---+---+---')
    print(board['ll'] + '|' + board['lm'] + '|' + board['lr'])

def check(board):
    return ((board['tl'] == board['tm'] == board['tr'] != '   ') or
            (board['ml'] == board['mm'] == board['mr'] != '   ') or
            (board['ll'] == board['lm'] == board['lr'] != '   ') or
            (board['tl'] == board['ml'] == board['ll'] != '   ') or
            (board['tm'] == board['mm'] == board['lm'] != '   ') or
            (board['tr'] == board['mr'] == board['lr'] != '   ') or
            (board['tl'] == board['mm'] == board['lr'] != '   ') or
            (board['ll'] == board['mm'] == board['tr'] != '   '))

while True:
    typ=input("What type of game u wanna play?\n'duo' or 'bot':")
    if typ in ['duo','bot']:
        print("Let's begin the game")
        break
    else:
        print("Invalid input")

turn='X'
i=1
choose=['tl', 'tm', 'tr', 'ml', 'mm', 'mr', 'll', 'lm', 'lr']

while True:
    pboard(board)
    if typ=='bot' and turn=='O':
        move=random.choice(choose)
        print("Bot chooses "+move)
    else:
        move=input(f"Turn {i} choose a position for {turn}:")
        
    if move not in choose:
        print("Invalid position\nTry again:")
        continue

    board[move]=' '+turn+' '
    choose.remove(move)
    i+=1
    #pboard(board)
    
    if check(board):
        winner="You" if typ=='bot' and turn=='X' else("Bot" if typ=='bot' else turn)
        print(f"\n{winner} wins the match!!!!!")
        break
    if len(choose)==0:
        print("\nIt's a tie\n")
        break
    turn = 'O' if turn=='X' else 'X'

print("Final board")
pboard(board)
    
    
