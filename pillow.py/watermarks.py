from PIL import Image, ImageDraw, ImageFont

image = Image.open("image.jpg")
draw = ImageDraw.Draw(image)
text = "Hello World"
 
font = ImageFont.truetype("arial.ttf", size=18)
 
draw.text((50, 50), text, font=font)
 
image.show()
