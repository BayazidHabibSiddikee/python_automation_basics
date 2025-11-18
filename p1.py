'''text = Hello World!
Im Bayazid HS
From the world of immortals
The fuckin BC '''
import pyperclip
#pyperclip.copy(text)
#pyperclip.copy()
text = pyperclip.paste()
#print(text)

lines = text.split('\n')
#print(lines)
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]


new = '\n'.join(lines)
print(new)
pyperclip.copy(new)
