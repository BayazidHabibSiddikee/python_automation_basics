import re
def stripx(x):
    return re.sub(r'^\s+|\s+$','',x)

print(stripx('      Hello World          '))


