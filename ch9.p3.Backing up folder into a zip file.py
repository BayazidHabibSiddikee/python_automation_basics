#! python3
import zipfile, os
def backup(folder):
    folder = os.path.abspath(folder) #Make sure the file is absolute

    #This should be used on existing file
    number = 1
    while True:
        zipfilename = os.path.basename(folder)+ '_'+str(number) + '.zip'
        if not os.path.exists(zipfilename):
            break
        number = number+1

    #Create a zip file
        print(f'Creating zipfile: {zipfilename}')
        backup = zipfile.ZipFile(zipfilename,'w')

        #Walk through folders
        for foldername, subfolders, filenames in os.walk(folder):
            print('Adding files in :'+folder)
            backup.write(foldername)

            for filename in filenames:
                newbase/os.path.basename(folder)+'_'
                if filename.startswith(newbase) and filename.endswith('.zip'):
                    continue
                backup.write(os.path.join(foldername,filename))
        backup.close()
        print('Done')
                
                                         
backup("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\Ai Swighat\\new_1.zip")
