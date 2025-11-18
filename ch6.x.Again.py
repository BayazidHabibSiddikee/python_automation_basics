td = [['apples', 'oranges', 'cherries', 'banana'], 
             ['Alice', 'Bob', 'Carol', 'David'], 
             ['dogs', 'cats', 'moose', 'goose']]

r_max =0
row=len(td)
col=len(td[0])

for i in td:
    for j in i:
        if len(j)>r_max:
            r_max = len(j)

for i in range(col):
    print()
    for j in range(row):
        print(td[j][i].rjust(r_max),end=' ')
