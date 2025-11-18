import os, re
folder = input("Enter folder path:").strip()
pattern = input("Enter regular expression pattern to search:").strip()


try:
    regex = re.compile(pattern)
except re.error as e:
    print("Invalid regex pattern: ",e)
    exit()

#Loop through all .txt files
for filename in os.listdir(folder):
    if filename.endswith('.txt'):
        filepath=os.path.join(folder,filename)
        try:
            file = open(filepath,'r')
            read = file.read()
            final=regex.findall(read)
            print(final)
        except:
            print(f"COuldn't read file: {filename}")
            
