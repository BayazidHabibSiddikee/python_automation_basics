def box(sym,width,height):
    if len(sym)!=1:
        raise Exception('Symbol can\'t be greater than 1')
    if width<=2:
        raise Exception('Width can\'t be smaller than 2')
    if height<=2:
        raise Exception('Height can\'t be smaller than 2')

    print(sym*width)
    for i in range(height-2):
        print(sym + ' '*(width-2) + sym)
    print(sym*width)

for a,b,c in (('*',4,4),('#',23,8),('0',20,5),('x',1,3),('zz',3,3)):
    try:
        box(a,b,c)
    except Exception as err:
        print('An exception has occur :'+ str(err))
                        
