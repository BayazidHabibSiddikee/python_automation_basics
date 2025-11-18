#collatz the impossible math problem
def collatz(number):
    print(number)
    if number ==1:
        return True #Whatever u give nothing happens
    elif number%2==0:
        return collatz(number//2)
    else:
        return collatz(number*3 + 1)
collatz(100)
