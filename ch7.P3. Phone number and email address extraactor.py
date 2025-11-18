import pyperclip

message = pyperclip.paste()

#message = "Hello there, this is Jonathan from BrightTech bright.tech.5432@gmail.com . If you have any inquiries regarding your account, feel free to reach out to our support team at supp_ort@brighttech.com or call us directly at (415) 555-2671. For partnership discussions, email maria.gonzalez@brighttech.com or dial our corporate line at 415-555-1987. If you're calling internationally, use +1-415-555-3333. You can also fax documents to 415.555.4040 or email them to fax@brighttech.com. For urgent issues, reach out to our emergency contact at (212)-555-9110 or email urgent@brighttech.com. Thank you for choosing BrightTech — where innovation meets reliability."

import re
num = re.compile(r'''(
(\+)?         #plus
(\d)?           #country code
(\s|-|\.)?     
(\d{3}|\(\d{3}\))    #Area code
(\s|-|\.)?
(\d{3}|\(\d{3}\))
(\s|-|\.)?
(\d{4}|\(\d{4}\))
)''',re.VERBOSE)

phone=num.findall(message)
a=[]
for i in phone:
    #print(i[0])
    a.append(i[0])

#print(phone)

email = re.compile(r'''(
((\w+\.)?)*
(\w+)
@(\w+).com
)''',re.VERBOSE|re.I)
names = email.findall(message)
for i in names:
   # print(i[0])
    a.append(i[0])

#print(a)
a = '\n'.join(a)
print(a)
pyperclip.copy(a)
