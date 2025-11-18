def string(a):
    b="'"
    for i in a:
        b+=str(i) + ','
    b+="'"
    return b

spam = ['apples', 'bananas', 'tofu', 'cats']
spam.append("kola")

print(string(spam))



print(string([1,2,3,4,5,6,7,'hello']))
