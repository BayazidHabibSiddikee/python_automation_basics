#! python3
# ch6.ProjectCopywebnameandpasswords.py

import sys
import pyperclip

PASSWORDS = {
    'email': 'F23456GHJKdfghj',
    'blog': 'Vasdfgh$%^&*567YfghjCVB',
    'luggage': '123456'
}

if len(sys.argv) < 2:
    print('Usage: python ch6.ProjectCopywebnameandpasswords.py [account]')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for account " + account + " copied to clipboard.")
else:
    print("There is no account named '" + account + "' in the database.")
