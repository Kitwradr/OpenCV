import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cat.jpg')

mask = np.zeros(img.shape[:2],np.uints8)

bgdModel = np.zeros((1,65),np.float64)

