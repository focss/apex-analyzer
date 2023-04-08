import cv2
import numpy as np
import os
import pytesseract
from PIL import Image
from func_cv_imread import cv_imread
from func_imgproc import Img_Similarity, BlackArea
import pandas as pd

def Cut_Ammo(Img):
    Img_Cut = Img[961:1000,1700:1785]
    return Img_Cut

def Binary_Ammo(img):
    img_binary = cv2.threshold(img, 215, 255, cv2.THRESH_BINARY_INV)[1]#二值化
    return img_binary

def AmmoOCR_ImgProcess(IMG):
    img = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)
    img = Cut_Ammo(img)
    img = Binary_Ammo(img)
    return img

def digit2(img):#百位数
    return img[3:34, 3:26]
def digit1(img):#十位数
    return img[3:34, 30:53]
def digit0(img):#个位数
    return img[3:34, 57:80]

def Ammo_Train_Generate():
    sourcefiledir = './AmmoTrainSource/'
    destfiledir = './AmmoTrainData/'
    for source in os.listdir(sourcefiledir):
        img = cv2.imread(sourcefiledir + source, 0)
        img_cut = Cut_Ammo(img)
        img_cut = Binary_Ammo(img_cut)
        cv2.imwrite(destfiledir + source, img_cut)


def Ammo_Recognize_TSR(IMG):
    img = AmmoOCR_ImgProcess(IMG)
    cv2.imwrite('./Temp/temp_ammo.png', img)
    pytesseract.pytesseract.tesseract_cmd = 'D:/Program Files/Tesseract-OCR/tesseract.exe'
    Text_Ammo = pytesseract.image_to_string(Image.open('./Temp/temp_ammo.png'))
    return Text_Ammo
    
def Ammo_Recognize_SingleDigit(img:np.ndarray):
    if BlackArea(img) < 80: return None
    reffiledir = './Ref/Ammo/'
    maxn = 10
    similarity = np.zeros([maxn,1], dtype=np.uint16)
    for i in range(maxn):
        img_Ref = cv2.imread(reffiledir + str(i) + '.png', 0)
        sim = Img_Similarity(img, img_Ref)
        similarity[i,0] = sim
    maxsimnum = np.max(similarity)
    maxsimname = np.where(similarity==np.max(similarity))[0][0]
    if maxsimnum < 300: return None
    return maxsimname
def Ammo_Recognize_cv(IMG:np.ndarray, digits:int):
    img = AmmoOCR_ImgProcess(IMG)
    AmmoNum = Ammo_Recognize_SingleDigit(digit0(img))
    if AmmoNum is None: return None
    if digits > 1:
        d1 = Ammo_Recognize_SingleDigit(digit1(img))
        if not d1 is None: AmmoNum += 10 * d1
    if digits == 3:
        d2 = Ammo_Recognize_SingleDigit(digit2(img))
        if not d2 is None: AmmoNum += 100 * d2
    return AmmoNum
def TestRun():
    i = 0
    testfiledir = './TestImage/'
    testsavedir = './AmmoEvaluateResult/'
    for filename in os.listdir(testfiledir):
        Img = cv_imread(testfiledir + filename)
        #ammo_num = Ammo_Recognize_TSR(Img)
        AmmoNum = Ammo_Recognize_cv(Img, 2)
        if AmmoNum is None: AmmoNum = 'None'
        img = AmmoOCR_ImgProcess(Img)
        cv2.imwrite(testsavedir + str(i) + '_' + str(AmmoNum) + '.png', img)
        i += 1
    
def Ammo_Ref_Generate():
    sourcefiledir = './Ref/Ammo_Original/'
    destfiledir = './Ref/Ammo/'
    for i in range(10):
        img = cv2.imread(sourcefiledir + str(i) + '.jpg', 0)
        img_cut = digit1(img)
        cv2.imwrite(destfiledir + str(i) + '.jpg', img_cut)
def Ammo_Ref_Evaluate():
    filedir = './Ref/Ammo/'
    maxn = 10
    similarity = np.zeros([maxn,maxn])
    black_area = np.zeros([maxn,1])
    for i in range(10):
        img1 = cv2.imread(filedir + str(i) + '.png', 0)
        for j in range(10):
            img2 = cv2.imread(filedir + str(j) + '.png', 0)
            sim = Img_Similarity(img1, img2)
            similarity[i,j] = sim
        black_area[i,0] = len(np.where(img1==0)[0])
    xd = pd.DataFrame(similarity)
    xd.to_excel('./Ref/Ammo_Similarity.xlsx', header=range(10))
    xd = pd.DataFrame(black_area)
    xd.to_excel('./Ref/Ammo_Ref_BlackArea.xlsx', header=None)
    
def Ammo_Evaluate(img:np.ndarray):
    reffiledir = './Ref/Ammo/'
    maxn = 10
    similarity = np.zeros([maxn,2], dtype=np.uint16)
    for i in range(maxn):
        img_Ref = cv2.imread(reffiledir + str(i) + '.png', 0)
        sim = Img_Similarity(img, img_Ref)
        similarity[i,1] = sim
        similarity[i,0] = i
    print('BlackArea:{}'.format(BlackArea(img)))
    print(similarity)
    similarity = similarity[:,1]
    maxsimnum = np.max(similarity)
    maxsimname = np.where(similarity==np.max(similarity))[0][0]
    print('Most Likely:{}, Similarity:{}'.format(maxsimname, maxsimnum))

if __name__ == '__main__':
    #Ammo_Train_Generate()
    TestRun()
    #Ammo_Ref_Generate()
    #Ammo_Ref_Evaluate()
    # img0 = cv2.imread('./AmmoEvaluateResult/204_8.jpg', 0)
    # img0 = digit0(img0)
    # cv2.imwrite('./Ref/Ammo/0.jpg', img0)
    
    # img = cv2.imread('./AmmoEvaluateResult/168_408.jpg', 0)
    # img = digit0(img)
    # img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)[1]
    # Ammo_Evaluate(img)
    # cv2.imshow('figure', img)
    # cv2.waitKey(0)
    # reffiledir = './Ref/Ammo/'
    # for i in range(10):
    #     img = cv2.imread(reffiledir + str(i) + '.jpg', 0)
    #     img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)[1]
    #     img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)[1]
    #     cv2.imwrite(reffiledir + str(i) + '.jpg', img)