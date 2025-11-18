import csv,os

a = open('/media/curse/New Volume/Study/Persona/Books/Phase 1 basics of programming/B1. Automate_the_Boring_Stuff_onlinematerials/automate_online-materials/example.csv')
b = csv.reader(a) #pointing on that location
#d = b
#c = list(b)

#print(c)


for i in b:
	print('row #'+str(b.line_num)+ ':  ' + str(i))
