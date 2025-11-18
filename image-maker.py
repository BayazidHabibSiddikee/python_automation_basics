import pyautogui
from PIL import Image
import time

# === Settings ===
image_path = "/home/curse/Downloads/file.enc"  # put your image file path
scale = 0.5             # resize factor (smaller = faster)
threshold = 128           # brightness cutoff
start_x, start_y = 300, 400  # top-left corner of drawing area

# Load and preprocess image
img = Image.open(image_path).convert("L")  # grayscale
img = img.resize((int(img.width * scale), int(img.height * scale)))

# Wait 5 seconds so you can focus GIMP window
print("Switch to GIMP! Starting in 5 seconds...")
time.sleep(5)

# Draw pixel by pixel
for y in range(img.height):
    for x in range(img.width):
        if img.getpixel((x, y)) < threshold:  # dark pixel
            pyautogui.moveTo(start_x + x, start_y + y)
            pyautogui.click()
