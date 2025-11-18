#! python3
import pyautogui as pt
print("ctrl + c or move the cursor to upper left corner for quit the program")

try:
	while True:
		sx,sy = pt.position()
		position = f'X: {str(sx).rjust(4)} Y: {str(sy).rjust(4)}'
		im=pt.screenshot()
		rgb = im.getpixel((sx,sy))
		position += f' RGB : ({str(rgb[0]).rjust(3)}, {str(rgb[1]).rjust(3)}, {str(rgb[2]).rjust(3)})'
		
		print(position,end='')
		print('\b'*len(position),end='',flush=True)
except KeyboardInterrupt:
	print('\Done')
