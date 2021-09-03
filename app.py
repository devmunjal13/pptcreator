
from ImageCreator import imageCreator
from PPTCreator import pptCreator


print("Started")
noOfImages = int(input("Please the number of image you want in your presentation \n"))
imgUrls=[]
for x in range(noOfImages):
    imgurl= input("Enter the path or url of Image {} \n".format(x+1))
    imgUrls.append(imgurl)
for y in range (len(imgUrls)):
    imageCreator.imageCreation(imgUrls[y],y+1)
    print(imgUrls[y]+"\n")
    pptCreator.createPPT('./Output/image{}.jpg'.format(y+1),"Home Assignment","Image {}".format(y+1))
pptCreator.savePPT()
# pptCreator.createPPT()
