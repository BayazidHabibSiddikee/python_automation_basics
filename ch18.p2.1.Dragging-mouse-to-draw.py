import pyautogui as pt
import time
time.sleep(4)
pt.click()
distance = 500
while distance>0:
	pt.dragRel(distance,0) #right
	distance -=10
	pt.dragRel(0,distance) #down
	pt.dragRel(-distance,0) #left
	distance -=10
	pt.dragRel(0,-distance) #Up
