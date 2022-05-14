from PIL import Image

image = Image.open('images.jpg')
image_1 = Image.open('image.jpg')
image1 = image.resize((1080, 1080))
image_2 = image_1.resize((1080, 1080)) 
image1.show()
image_2.show()

