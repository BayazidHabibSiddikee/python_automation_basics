import os
for folderName, subfolders, filenames in os.walk('C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312'):
    #print('The current folder is ' + folderName)
    #for subfolder in subfolders:
        #print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        if filename.endswith('.py'):
            print('FILE INSIDE ' + folderName + ': '+ filename)#print('')
