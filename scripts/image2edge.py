'''
author: Cong Li
Time: 11-19-20
特征提取，转化为 pix2pix_tensorflow 的训练数据集
使用方法见 REDAME.md
'''
import cv2
import numpy as np
import glob
import argparse
from progress.bar import Bar


def get_file_name(image_dir):
    file_name = glob.glob(image_dir + '/*.jpg')
    return file_name


def out_edges(file_names, output_dir, width=600, height=800):
    bar = Bar('边缘提取进度如下：', max=len(file_names))
    name = 1
    for file in file_names:
        print(file)
        img = cv2.imread(file)
        sp = img.shape
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        _, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        canvas = np.zeros((sp[0], sp[1], 3), dtype="uint8")
        canvas[:, :, :] = (255, 255, 255)
        im = cv2.drawContours(canvas, contours, -1, (0, 0, 0), 2)
        # im = cv2.resize(im, (width, height))
        cv2.imwrite(output_dir + file.split('/')[-1], im)
        name += 1
        bar.next()
    bar.finish()


def out_pixdataset():
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-width")
    parser.add_argument("-height")
    parser.add_argument("-image_dir")
    parser.add_argument("-output")

    args = parser.parse_args()
    image_dir = args.image_dir
    file_names = get_file_name(image_dir)
    output_dir = args.output
    out_edges(file_names, output_dir)
