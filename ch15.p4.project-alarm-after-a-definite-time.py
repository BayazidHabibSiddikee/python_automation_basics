#! /usr/bin/env python3
import subprocess as SP
import time, sys
from colorama import Style, Fore

timeleft = 5
while timeleft>0:
	print(Fore.RED+str(timeleft)+ Style.RESET_ALL)
	time.sleep(1)
	timeleft -=1

#Lets play the sound
SP.Popen(['vlc-wrapper',"automate resources/alarm.wav"])
#xdg-open can't be used as root but 'vlc-wrapper' can for vlc media
sys.exit()
