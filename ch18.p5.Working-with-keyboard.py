import pyautogui as pt
import time
def comment_after_delay():
	pt.click(200,200)
	time.sleep(2)
	pt.typewrite("In Idle, Alt-3 comments out a line",0.1)
	time.sleep(1)
	pt.hotkey(['ctrl','a'])
	time.sleep(1)
	pt.hotkey(['ctrl','c'])
	time.sleep(1)
	for i in range(30):
		pt.hotkey(['ctrl','v'])
		pt.hotkey(['shift','enter'])
	
comment_after_delay()
