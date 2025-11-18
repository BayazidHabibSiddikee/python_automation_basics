from PIL import Image , ImageDraw
path = '/home/curse/Pictures/Learn-button.xcf'
#Setting
scale = 0.8
threshold = 128
img = Image.open(path).convert("L") #grayscale
img = img.resize((int(img.width*scale),int(img.height*scale)))

#Creating an image as im
im = Image.new('RGBA',(img.width,img.height),'white')
draw = ImageDraw.Draw(im)

for y in range(img.height):
	for x in range(img.width):
		if img.getpixel((x,y))<threshold: #Consider them as black
			draw.point((x,y),fill='black')
im.save('learn-button.png')
