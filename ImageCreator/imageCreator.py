from wand.image import Image, COMPOSITE_OPERATORS
from wand.drawing import Drawing
from wand.display import display

def imageCreation(img,i) :
    img1 = Image(filename ='./Images/nike_black.png').clone()
    img2 = Image(filename = img).clone()
    with Drawing() as draw:
        draw.composite(operator = 'darken', left = 20, top = 30,
                    width = img1.width//2, height = img1.height//2, image = img1)
        draw(img2)
        img2.save(filename ="./Output/image{}.jpg".format(i))
        