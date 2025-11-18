import re
phone = re.compile(r'''(
(\d{3}|\(\d{3}\))?  #Area code
(\s|-|\.)?
\d{3}
(\s|-|\.)?
\d{4} #Last four digit
(\s*(ext|x|ext.)\s*\d{2,5})?
)''',re.VERBOSE)

message = "Hello there, this is Jonathan from BrightTech. If you have any inquiries regarding your account, feel free to reach out to our support team at support@brighttech.com or call us directly at (415) 555-2671. For partnership discussions, email maria.gonzalez@brighttech.com or dial our corporate line at 415-555-1987. If you're calling internationally, use +1-415-555-3333. You can also fax documents to 415.555.4040 or email them to fax@brighttech.com. For urgent issues, reach out to our emergency contact at (212)-555-9110 or email urgent@brighttech.com. Thank you for choosing BrightTech — where innovation meets reliability."

num = phone.findall(message)
print(num)
