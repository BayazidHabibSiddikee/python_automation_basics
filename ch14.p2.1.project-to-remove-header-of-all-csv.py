#! python3
import os, csv, shutil

os.makedirs('withoutheader1',exist_ok = True)
os.makedirs('withoutheader2',exist_ok = True)

#Loop through cwd to find .csv
for file in os.listdir('.'):
	if not file.endswith('.csv'):
		continue
	print('Removing header from '+file)
	
	a = open(file) #reading only
	#a = open('withoutheader/file')
	b = csv.reader(a)
	c = open(os.path.join('withoutheader1',file),'w',newline='') #a new file
	d = csv.writer(c)
	
	for i in b:
		if b.line_num == 1:
			continue
		print(str(b.line_num)+str(i))
		d.writerow(i)
		
	
	#Let's do in another way
	a_file = open(os.path.join('withoutheader2',file),'w',newline='')
	f = csv.writer(a_file)
	e = []
	for i in b:
		if b.line_num==1:
			continue
		e.append(i)
		f.writerow(i)
		print(i)
		
		
	a.close()
	c.close()
