#! python3
import os, shutil
def delete(x):
    for foldername,subfoldername, files in os.walk(x):
        for file in files:
            path = os.path.join(foldername,file)
            if os.path.getsize(path)>= 320000:
                print(f'Deleting path: {path} of file: {os.path.getsize(path)}')
                os.unlink(path)
                

delete('C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\Ai Swighat')
