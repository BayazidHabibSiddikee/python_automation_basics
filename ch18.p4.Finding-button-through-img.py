import pyautogui
import cv2

print("cv2 version:", cv2.__version__)
box = pyautogui.locateOnScreen('/home/curse/Pictures/button.png', confidence=0.8)
print("Found:", box)
