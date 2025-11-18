import sys, pyperclip
'''
account = sys.argv[1]
print("Oh you are "+ account)
'''

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}


if len(sys.argv)<2:
    print('Usage: py pw.oy [account] - copy account password')
    sys.exit()

account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for the "+ account + ' copied to clipboard')
else:
    print("There is no account name: " + account)
