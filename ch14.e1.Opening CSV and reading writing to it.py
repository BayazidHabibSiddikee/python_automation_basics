import os , csv

a = open(os.getcwd()+'\\automate resources\\example.csv')
b = csv.reader(a)
'''
c = list(b)
print(c)
''' # can do separetely but if uncomment second way becomes NULL -_-

#Second way
j = 1
for i in b:
    print('Row #'+str(j)+ ' '+ str(i))
    j+=1
        
