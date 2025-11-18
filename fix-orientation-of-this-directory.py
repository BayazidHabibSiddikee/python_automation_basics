import os

for filename in os.listdir():
	if filename.startswith('ch'):
		new =open('B1.'+ filename,'w')
		print(filename +' changed to '+ new)
		content = open(filename,'r')
		for i in content:
			new.write(i)
		new.close()
		content.close()
	
