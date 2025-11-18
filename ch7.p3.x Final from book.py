#! python3
import re, pyperclip

phone = re.compile(r'''(
(\+\d)? #country code
(\s|-|\.)?
(\d{3}|\(\d{3}\))?                # area code
(\s|-|\.)?                        # separator
(\d{3})                           # first 3 digits
(\s|-|\.)                         # separator
(\d{4})                           # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
)''', re.VERBOSE)

email = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
\.[a-zA-Z]{2,}
)''',re.VERBOSE)

text = str(pyperclip.paste())
num = phone.findall(text)
mail = email.findall(text)

last=[]
for i in num:
    last.append(i[0])
for i in mail:
    last.append(i)
last = '\n'.join(last)

if len(last)>0:
    print("Copied to clipboard:\n" +last)
    pyperclip.copy(last)
else:
    print('No phone number or emails have found')
