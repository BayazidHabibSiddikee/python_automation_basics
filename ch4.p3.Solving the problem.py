import copy
a=[1,2,3,4,5,6]
b = a
b[2]='hell'
print(a)
print(b)

c = copy.copy(a)
c[2]='world'
print(a)
print(c)

#deepcopy which is more great than copy
d = copy.deepcopy(a)
d[2]='kelly'
print(a)
print(d)
