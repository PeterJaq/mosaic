import cv2
import numpy as np
import os

IMAGE_DIR = "./picture/sample.jpg"
MOSAIC_DIR = "./model/"
COLOR_DIR = "./temp/"
IMAGE_SIZE = 40
CELL_SIZE = 177
OUT_IMAGE_SHAPE = (CELL_SIZE*IMAGE_SIZE, CELL_SIZE*IMAGE_SIZE, 3)
IMG_COLOR_LIST = {}

def load_mosaic_cell(dir = MOSAIC_DIR, ipImgNo = "A", Model = "BrainyColor"):
    """

    :param MOSAIC_DIR: The Mosaic_dir
    :param ipImgNo: Which small picture use, Row: 1, 2, 3 Line:A, B, C
    :return: The mosaic fund of picture

    The cell size is 354 * 354
    """

    if Model == "BrainyColor":
        input_Dir = dir + Model + "/" + ipImgNo + ".jpg"
        img = cv2.imread(input_Dir)
        return img

def find_color(color):
    tmp = 500
    select_color = 0
    for _ in IMG_COLOR_LIST.keys():
        if abs(int(color) - _) < tmp:
            tmp = abs(int(color) - _)
            select_color = _

    sct_color_path = IMG_COLOR_LIST.get(select_color)
    PATH = COLOR_DIR + sct_color_path
    imgColor = cv2.imread(PATH)
    sct_color = imgColor[0][0]

    return sct_color




def cell_2_img(empty_img, w, h, color, model, colorful="False"):
    cell_img = load_mosaic_cell(ipImgNo=model)
    if model == "A" or model == "1":
        color_img = np.zeros(cell_img.shape, np.uint8)
        if colorful == "False":
            color_img[:, :] = color
        else:
            color_img[:, :] = find_color(color)
        cell_img = cv2.addWeighted(cell_img, 0.7, color_img, 0.6, -100)
        empty_img[h*CELL_SIZE:(h+2)*CELL_SIZE, w*CELL_SIZE:(w+2)*CELL_SIZE] = cell_img
    elif model == "B":
        #if h == 38 and w = 16
        color_img = np.zeros(cell_img.shape, np.uint8)
        if colorful == "False":
            color_img[:, :] = color
        else:
            color_img[:, :] = find_color(color)
        cell_img = cv2.addWeighted(cell_img, 0.7, color_img, 0.6, -100)
        empty_img[h * CELL_SIZE:(h + 1) * CELL_SIZE, w * CELL_SIZE:(w + 2) * CELL_SIZE] = cell_img
    elif model == "2":
        color_img = np.zeros(cell_img.shape, np.uint8)
        if colorful == "False":
            color_img[:, :] = color
        else:
            color_img[:, :] = find_color(color)
        cell_img = cv2.addWeighted(cell_img, 0.7, color_img, 0.6, -100)
        empty_img[h * CELL_SIZE:(h + 2) * CELL_SIZE, w * CELL_SIZE:(w + 1) * CELL_SIZE] = cell_img
    elif model == "C" or "3":
        color_img = np.zeros(cell_img.shape, np.uint8)
        if colorful == "False":
            color_img[:, :] = color
        else:
            color_img[:, :] = find_color(color)
        cell_img = cv2.addWeighted(cell_img, 0.7, color_img, 0.6, -100)
        empty_img[h * CELL_SIZE:(h + 1) * CELL_SIZE, w * CELL_SIZE:(w + 1) * CELL_SIZE] = cell_img

    return empty_img

def scan_picture(img, empty_img):

    img_w = img.shape[0]
    img_h = img.shape[1]

    new_w = empty_img[0]
    new_h = empty_img[1]

    colorful = "True"


    for h in range(0, img_w, 2):
        for w in range(0, img_h, 2):
            img_cell_tl = img[h][w]
            img_cell_tr = img[h][w+1]
            img_cell_dl = img[h+1][w]
            img_cell_dr = img[h+1][w+1]



            print("H = %d, W = %d" % (h, w))

            if (w + h) % 4 != 0:
                """ line cell """
                if img_cell_dl == img_cell_tr == img_cell_dr == img_cell_tl:
                    empty_img = cell_2_img(empty_img, w, h, img_cell_tl, model="A", colorful=colorful)
                    #print(empty_img.shape)
                elif img_cell_tl == img_cell_tr:
                    empty_img = cell_2_img(empty_img, w, h, img_cell_tl, model="B", colorful=colorful)
                    empty_img = cell_2_img(empty_img, w, h+1, img_cell_dl, model="C", colorful=colorful)
                    empty_img = cell_2_img(empty_img, w+1, h+1, img_cell_dr, model="C", colorful=colorful)
                elif img_cell_dl == img_cell_dr:
                    empty_img = cell_2_img(empty_img, w, h+1, img_cell_dl, model="B", colorful=colorful)
                    empty_img = cell_2_img(empty_img, w, h, img_cell_tl, model="C", colorful=colorful)
                    empty_img = cell_2_img(empty_img, w+1, h, img_cell_tr, model="C", colorful=colorful)
                else:
                    empty_img = cell_2_img(empty_img, w, h, img_cell_tl, model="C", colorful=colorful)
                    empty_img = cell_2_img(empty_img, w+1, h, img_cell_tr, model="C", colorful=colorful)
                    empty_img = cell_2_img(empty_img, w, h+1, img_cell_dl,model="C", colorful=colorful)
                    empty_img = cell_2_img(empty_img, w+1, h+1, img_cell_dr, model="C", colorful=colorful)
            else:
                """ row cell """
                if img_cell_dl == img_cell_tr == img_cell_dr == img_cell_tl:
                    empty_img = cell_2_img(empty_img, w, h, img_cell_tl, model="1", colorful=colorful)
                elif img_cell_tl == img_cell_dl:
                    empty_img = cell_2_img(empty_img, w, h, img_cell_tl, model="2", colorful=colorful)
                    empty_img = cell_2_img(empty_img, w+1, h, img_cell_tr, model="3", colorful=colorful)
                    empty_img = cell_2_img(empty_img, w+1, h+1, img_cell_dr, model="3", colorful=colorful)
                elif img_cell_tr == img_cell_dr:
                    empty_img = cell_2_img(empty_img, w+1, h, img_cell_tr, model="2", colorful=colorful)
                    empty_img = cell_2_img(empty_img, w, h, img_cell_tl, model="3", colorful=colorful)
                    empty_img = cell_2_img(empty_img, w, h+1, img_cell_dl, model="3", colorful=colorful)
                else:
                    empty_img = cell_2_img(empty_img, w, h, img_cell_tl, model="3", colorful=colorful)
                    empty_img = cell_2_img(empty_img, w+1, h, img_cell_tr, model="3", colorful=colorful)
                    empty_img = cell_2_img(empty_img, w, h+1, img_cell_dl, model="3", colorful=colorful)
                    empty_img = cell_2_img(empty_img, w+1, h+1, img_cell_dr, model="3", colorful=colorful)

    return empty_img




if __name__ == '__main__':

    img = cv2.imread(IMAGE_DIR, cv2.IMREAD_REDUCED_GRAYSCALE_2)
    size = img.shape
    img_tmp = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))


    for filename in os.listdir(r"./temp"):
        PATH = "./temp/" + filename
        imgColor = cv2.imread(PATH, cv2.IMREAD_REDUCED_GRAYSCALE_8)
        IMG_COLOR_LIST.setdefault(imgColor[0][0], filename)

    emptyImage = np.zeros(OUT_IMAGE_SHAPE, np.uint8)
    out_img = scan_picture(img_tmp, emptyImage)
    out_img = cv2.resize(out_img, img.shape)

    cv2.imshow("out img", out_img)
    cv2.waitKey(0)
