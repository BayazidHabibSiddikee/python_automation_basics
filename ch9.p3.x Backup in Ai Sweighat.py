#! python3
import os, zipfile

def backup(folder):
    folder = os.path.abspath(folder)
    num =1
    while True:
        name = os.path.basename(folder)+'_'+str(num)+'.zip'
        if not os.path.exists(os.path.join(os.path.dirname(folder),name)):
            break
        else:
            num=num+1
    print(f'Zipfile created name: {name}')
    zipp = zipfile.ZipFile(os.path.join(os.path.dirname(folder),name),'w')
    
    for files in os.listdir(folder):
        zipp.write(os.path.join(folder,files))
    #print(f'Content in the file: {zipp.namelist()}')
    zipp.close()
    print("done..")


realfile = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\Ai Swighat\\Als python book'
#os.chdir(realfile)
backup(realfile)
