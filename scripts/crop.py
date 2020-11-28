from PIL import Image

L = [(11, 37, 708, 1337), (11, 1357, 708, 2657), (11, 2677, 708, 3977)]
i = 1
img = Image.open("../static/origin/6.jpg")
for coordinate in L:
    cropped = img.crop(coordinate)
    cropped.save("./" + str(i) + '.jpg')
    i += 1
