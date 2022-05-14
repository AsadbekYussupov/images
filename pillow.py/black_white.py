from PIL import Image

image = Image.open('images.jpg')
image_1 = Image.open('image.jpg')
image1 = image.convert("L")
image_2 = image_1.convert("L")
image1.show()
image_2.show()

