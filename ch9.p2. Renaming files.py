import re, os, shutil
def check(x): #check America and convert to euro
    pat = re.compile(r"""
    ^(.*?)               # prefix before date
    ((0|1)?\d)-          # month part (group 2)
    ((0|1|2|3)?\d)-      # day part   (group 4)
    ((19|20)\d\d)        # year part  (group 6)
    (.*?)$               # suffix after date
    """,re.VERBOSE)
    
    y = pat.search(x)
    if y==None:
        return
    else:
        amer = ultimate(x)
        euro = ultimate(f'{y.group(1)}{y.group(4)}-{y.group(2)}-{y.group(6)}{y.group(8)}')
        print(f"Converted from {amer} to {euro}")
    

def ultimate(x): #Ultimate road -_-
    cwd = os.getcwd()
    return os.path.join(cwd,x)

for i in os.listdir():
    check(i)
    
