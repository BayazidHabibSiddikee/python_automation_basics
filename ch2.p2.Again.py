import re
'''
def search(x):
    if len(x)!=12:
        return False
    for i in range(0,3):
        if not x[i].isdecimal():
            return False
    if x[3]!='-':
        return False
    for i in range(4,7):
        if not x[i].isdecimal():
            return False
    if x[7]!='-':
        return False
    for i in range(8,12):
        if not x[i].isdecimal():
            return False
    return True
'''
message= 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
style = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
'''
for i in range(len(message)):
    chunk = message[i:i+12]
    if search(chunk):
        print("Number found: "+chunk)
'''
for i in range(len(message)-11):
    chunk = message[i:i+12]
    num=style.search(chunk)
    #print(chunk)
    if num:
        print("Found the number: "+num.group())
