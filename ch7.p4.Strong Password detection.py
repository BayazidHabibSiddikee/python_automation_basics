import re
def strong(x):
    first = re.compile(r'.{8,}')
    sec = re.compile(r'[a-z]')
    third = re.compile(r'[A-Z]')
    fourth = re.compile(r'\d')
    if (first.search(x) and sec.search(x) and third.search(x) and fourth.search(x)):
        print("The password is strong")
    else:
        print('Too weak like u')

strong('Hello1234')
strong('dghg')
strong('AdfghH35#$%^&')
