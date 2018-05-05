import cv2
import numpy as np
import os

def read_cell(cell_sample):
    img_path = "./model/BrainyColor/%s.jpg" % cell_sample
    img = cv2.imread(img_path)

    return img

def read_color(color_index):
    color_path = "./temp/%s.jpg" % color_index
    color = cv2.imread(color_path)
    src_color = color[0][0]
    return src_color

if __name__ == '__main__':

    cell_img = read_cell("A")
    color_img = np.zeros(cell_img.shape, np.uint8)
    color_img[:, :] = read_color("6")
    out_img = cv2.addWeighted(cell_img, 0.7, color_img, 0.6, -100)
    cv2.imwrite('./out/6.jpg', out_img)
    cv2.imshow("out img", out_img)
    cv2.waitKey(0)

