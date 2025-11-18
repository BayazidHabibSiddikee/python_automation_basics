import csv
a = open('ch14.p1.4.pracitse.csv','w')
b = csv.writer(a,delimiter='#',lineterminator='\n') # to change those shits -_-

c = ['a','b','c','d']
d = ['a','b','c','d']
e = ['a','b','c','d']
f = ['a','b','c','d']
g = ['a','b','c','d']
h = ['a','b','c','d']

x = [c,d,e,f,g,h]

for i in x:
	b.writerow(i)


a.close()
