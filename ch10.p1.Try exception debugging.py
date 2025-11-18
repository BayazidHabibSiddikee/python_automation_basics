def box(a,width,height):
    if len(a) !=1:
        raise Exception('Symbol must be a single character string.')
    if width<= 2:
        raise Exception('Width must be greater than 2')
    if height<=2:
        raise Exception('Height must be greater than 2')
    print(a*width)
    for i in range(height-2):
        print(a+(' '*(width-2)) + a)
    print(a*width)

for a,w,h in (('*',4,4),('0',20,5),('x',1,3),('zz',3,3)):
    try:
        box(a,w,h)
    except Exception as e:
        print('An Exception happened: '+str(e))
