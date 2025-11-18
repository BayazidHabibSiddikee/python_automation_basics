#! python3
import os, re

def searched(x,ext,content): 
    '''typ = re.compile(r'\w+\.'+ext)
    result = typ.findall(x)'''
    if x.endswith(f'.{ext}'):
        file = open(x,'r')
        read = file.read()
        if content in read:
            print(f'FIle name:{file} and contents:\n{read}')
        file.close()

print('Wanna know contents:?')
a = input("yes or no if you don't know any folders name:")
if a=='yes':
    path=input("Enter folders name with path: ")
else:
    #path = os.getcwd()
    ls = os.getcwd().split(os.path.sep)
    print(ls)
    path =input("Name any folder?\n:")
    new =[]
    if path in ls:
        for i in range(len(ls)):
            new.append(ls[i])
            if ls[i]==path:
                break
    new = '\\\\'.join(new)
    print(new)  #File paths with double slash
    print(os.listdir(new))
    ext = input("What is the file extension?\n:")
    con = input("What contents u want to find?\n:")
    for i in os.listdir(new):
        searched(os.path.join(new,i),ext,con)

#fd = find directory
#fd = os.path.dirname(path) #fd is wrong here so comment it would be better
#print(fd)

