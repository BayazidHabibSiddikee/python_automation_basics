import re
message= 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')


for i in range(len(message)-11):
    msg = message[i:i+12]
    chunk= phone.search(msg)
#mo = phone.search(message)
    if chunk:
        print(chunk.group())


'''
mo = phone.search(message)
print(mo.group())
'''
