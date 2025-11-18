import logging
logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s -%(levelname)s -%(message)s')
################################################## time           Debug         logging.debug(msg)
logging.debug('Start of the program')

def factorial(n):
    logging.debug(f'Start of factorial {n}')
    total =1
    for i in range(1,n+1):
        total*=i
        
        logging.debug(f'i is {i} total is {total}')

    logging.debug(f'End of the factorial loop of {n}')
    return total
print(factorial(5))
logging.debug('End of the program')
logging.disable(logging.CRITICAL)
