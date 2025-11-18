#! python3
import pyperclip
text = pyperclip.paste() #It'll be a text with '\n' so need to replace '\n' with * or #
#pyperclip.copy()


lines = text.split('\n') #It will return a list
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
    
