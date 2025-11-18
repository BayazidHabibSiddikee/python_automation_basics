import csv
a = open('p1.1.write.csv')
b = csv.reader(a)
for i in b:
	print('row #'+str(b.line_num)+str(i))
a.close()
