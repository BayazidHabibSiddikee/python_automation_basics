import sys
def spam(a):
    try:
        return 42/a
    except ZeroDivisionError:
        print("Invalid argument")
        return None
while True:
    print("Enter a num and to exit write exit: ")
    name = input()
    if name == "exit":
        sys.exit()
    else:
        a = float(spam(float(name)))
        print("Divided to 42 by " + str(name) + " we get " + str(a))

            
