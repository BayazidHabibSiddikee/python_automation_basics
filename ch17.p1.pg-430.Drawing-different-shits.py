from PIL import Image , ImageDraw
im = Image.new('RGBA',(200,200),'white')
draw = ImageDraw.Draw(im)
draw.line([(0,0),(199,0),(199,199),(0,199),(0,0)],fill='black')
draw.rectangle((20,30,60,60),fill='red')

for i in range(100,200,10):
	draw.line([(1,0),(200,i-100)],fill='green')
im.save('drawing.png')	
print("done")

