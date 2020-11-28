import glob
from PIL import Image

file_name = glob.glob('../static/hd_crop_single/*.jpg')

i = 1
for f in file_name:
    img1 = Image.open(f)
    target = Image.new('RGB', (img1.size[0] * 2, img1.size[1]))
    result = f.split('/')
    result[2] = 'hd_crop_edge'
    img2 = Image.open('/'.join(result))
    target.paste(img1, (0, 0, img1.size[0], img1.size[1]))
    target.paste(img2, (img1.size[0], 0, img1.size[0] * 2, img1.size[1]))
    target.save("../static/hd_combine_pix2pix/" + str(i) + '.jpg')
    i += 1
