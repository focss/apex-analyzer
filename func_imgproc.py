import cv2
import numpy as np
def BlackArea(img):#阴影面积
    return len(np.where(img==0)[0])

def WhiteArea(img):#白区面积
    return len(np.where(img==255)[0])

def Img_Similarity(img1, img2):
    comp = img1 == img2
    sim = len(np.where(comp==True)[0])
    return sim