table = [['apples', 'oranges', 'cherries', 'banana'], 
             ['Alice', 'Bob', 'Carol', 'David'], 
             ['dogs', 'cats', 'moose', 'goose']]


z=0
col=0
row=0
#new=[]
for x in range(len(table)):
    row+=1
    col = len(table[x])
    for y in range(len(table[x])):
        #print(table[x][y])     
        if(z<len(table[x][y])):
            z=len(table[x][y])
            #new=table[x][y].appened()

            
#print(col,row,z)


for i in range(col):
    print()
    for j in range(row):
        print(table[j][i].rjust(z),end=' ')
