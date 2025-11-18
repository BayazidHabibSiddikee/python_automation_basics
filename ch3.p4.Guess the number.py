import random
print("I'm thinking a number between 1 to 20\nTry to guess the number to break the loop and see my message")
secret= random.randint(1,20)
while True:
    print("Number:")
    num = int(input())
    if num == secret:
        print("What the heck u did it and the number is "+ str(num))
        break
    elif num<=secret:
        print("Number u entered "+ str(num)+ " is too low")
    else:
        print("Number u entered " + str(num) + " is too high")
            
print("Secret message(Fuck u)")
