#! /usr/bin/lib/python3
import pyautogui as pt

print("ctrl + C to quit else move cursor to (0,0)")
try:
	while True:
		x,y = pt.position()
		#size = pt.size()
		position = 'X: '+ str(x).rjust(4) + 'Y: '+ str(y).rjust(4)
		#print("Screen size: " + str(size))
		print(position,end='')
		print('\b'* len(position),end='',flush=True)
except KeyboardInterrupt:
	print("\Done")
