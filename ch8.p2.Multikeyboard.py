#! python3
import sys, shelve, pyperclip

mcb = shelve.open('mcb')
if len(sys.argv)==3 and sys.argv[1].lower=='save':
    mcb[sys.argv[2]]==pyperclip.paste()
elif len(sys.argv)==2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(list(mcb.keys()))
    elif sys.argv[1]  in mcb:
        pyperclip.copy(mcb[sys.argv[2]])
    
mcb.close()
