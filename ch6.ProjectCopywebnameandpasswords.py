#! python3
#pw.py -An insecure password locker program

PASSWORDS={'email':'F23456GHJKdfghj',
           'blog':'Vasdfgh$%^&*567YfghjCVB',
           'luggage':'123456'}

import sys
if len(sys.argv)<2:
    print('Usage: pythonn pw.py[account] - copy account password')
    sys.exit()

account=sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for account "+account+' copied to clipboard')
else:
    print("There is no such account named "+account)
