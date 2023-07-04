from PIL import Image
import numpy as np

def black_white(image, size):
    #img = Image.open(image)
    #print(image)
    img_data = image.getdata()
    #print(img_data)
    lst = []

    for i in img_data:

        test = i[0]*0.2125+i[1]*0.7174+i[2]*0.0721
        lst.append(test)
        #print(lst)

    #print(lst)
    newImg = Image.new("L", size)
    newImg.putdata(lst)

    newImg.save("black_white.jpg")

    return np.array(newImg)

'''img = Image.open("teste.jpg")
img_data = img.getdata()

black_white(img_data, img.size)
print("img data: ", img_data)
print("end data")
print("img size: ", img.size)
print("end size")
print(black_white(img_data, img.size))'''