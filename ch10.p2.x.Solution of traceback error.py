import traceback
try:
    raise Exception('This is error message')
except:
    errorfile = open('errorinfo.txt','w')
    errorfile.write(traceback.format_exc())
    errorfile.close()
    print(f'Traceback info was written to {errorfile} file')
    
