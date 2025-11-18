import random, logging
#logging.disable(logging.CRITICAL)
logging.basicConfig(filename=r'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\Ai Swighat\\ch10.p6.Log files.txt',
level = logging.DEBUG,
format=f'%(asctime)s |%(levelname)-8s |%(message)s')
logging.debug('Starting the program')

guess=''

logging.info(f'Guess: ({guess})')
while guess not in ('heads','tails'):
    #logging.debug(f'Starting while loop with guess: ({guess})')

    guess=input('Guess the coin toss!\nEnter heads or tails: ').lower()
    #assert (guess=='heads' or guess=='tails'),'Value of guess must be heads or tails'
    logging.debug(f'User input in while loop: {guess}')
    
toss = random.choice(['heads','tails']) #0 = tails
logging.debug(f'From computer guess: ({toss})')

if toss==guess:
    print('You got it')
else:
    print('Nope! Guess again:')
    guess = input().lower()
    
    logging.debug(f'Starting while loop with guess: ({guess})')
    assert (guess=='heads' or guess=='tails'),'Value of guess must be heads or tails'
    
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
