def new(a):
    a.append("Hello")

b = [1,2,3,4,5]
print(b)
new(b)

print(b)


a=b
a[2]='world'

#new(b)
print(b)  #I only changed a but it shows in both of the list as List in python uses reference values

print(a)
