import sys
def div(a):
    return 42/a
while True:
    print("Enter a num and to exit write exit: ")
    value = input()
    if value =="exit":
        sys.exit()
    try:
        print("Divided "+ str(value) + " to 42 :" + str(div(float(value))))
    except ZeroDivisionError:
        print("Try again bruh")
        #continue
            
    
