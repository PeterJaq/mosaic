import cv2
import numpy as np
import os

IMAGE_DIR = "./temp/sample.jpg"

if __name__ == '__main__':

    img = cv2.imread(IMAGE_DIR, cv2.IMREAD_GRAYSCALE)
    for filename in os.listdir(r"./temp"):
        PATH = "./temp/" + filename
        imgColor = cv2.imread(PATH, cv2.IMREAD_REDUCED_GRAYSCALE_8)

        print("filename:%s, gray:%d"%(filename, imgColor[0][0]))

