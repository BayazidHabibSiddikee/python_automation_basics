import shutil, os, re
pattern = re.compile(r"""^(.*?) #All are text before the date
((0|1)?\d)-    #one or two digit for the month
((0|1|2|3)?\d)- #one/2 digit for the day
((19|20)\d\d) #Four digit for year
(.*?)$ #All text after the date
""",re.VERBOSE)

for file in os.listdir('.'):
    mo = pattern.search(file)

    if mo==None:
        continue
    #print(mo.groups())

    before = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    after = mo.group(8)



    euro = before + day+'-' + month+'-' + year + after
    ful_abs_path = os.path.abspath('.')
    amer_path = os.path.join(ful_abs_path, file)
    euro_path = os.path.join(ful_abs_path, euro)
    print(f"Renaming file: {amer_path} to {euro_path}")
    
