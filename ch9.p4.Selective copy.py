#! python3
import os, shutil
def cope(folder):
    for foldername, subfolders, files in os.walk(folder):
        for file in files:
            print(file)
            if file.endswith('.png'):
                source = os.path.join(foldername,file)
                shutil.copy(source,'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\Ai Swighat\\Als python book')
cope('C:\\Users\\HP\\OneDrive\\Pictures\\Screenshots')
