import csv
a = open('p1.1.write.csv','w',newline='')
b = csv.writer(a)

b.writerow(['spam','eggs','ham'])
b.writerow([1,2,3])

a.close()
