
# # #####################################################
# import numpy as np
# import cv2
# color = [255, 100, 0]
# pixel = np.uint8([[color]])
# hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)  # BGR을 HSV 좌표로 변경
# hsv = hsv[0][0]
# print("bgr: ", color)
# print("hsv: ", hsv)

# BLUE  + GREEN + RED
# RGB888(24), RGB565(16)
# 색 공간 COLOR SPACE --> 가상 혼합 방식 색상 s 작을수록 흰색
# v 색상의 밝은 정도 숫자가 0에 가까울수록 검정, 1일수록 흰색

# # #####################################################

import cv2
img_color = cv2.imread('img.jpg')
h,w = img_color.shape[:2]  # 이미지의 높이 가로를 가지고 온다
img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)  # HSV Image로 변경

l_blue = (120-50,50,50)  # 너무 어두워서 검은색에 가까운 값과
u_blue = (120+50,200,200) # 너무 밝아서 흰색에 가까운 값 제거

img_mask = cv2.inRange(img_hsv, l_blue, u_blue)
img_result = cv2.bitwise_and (img_color, img_color, mask = img_mask)  #마스크를 이용하여 제거

cv2.imshow('img_hsv', img_hsv)
cv2.imshow('img_color', img_color)
cv2.imshow('img_mask', img_mask)
cv2.imshow('img_result',img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2
# img_color = cv2.imread('img.jpg')
# height,width = img_color.shape[:2]  # 이미지의 높이와 너비를 가지고옴
# img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)
# lower_blue = (120-10, 30, 30)
# upper_blue = (120+10, 255, 255)
# img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
# img_result = cv2.bitwise_and(img_color, img_color, mask = img_mask)
# cv2.imshow('img_color', img_color)
# cv2.imshow('img_mask', img_mask)
# cv2.imshow('img_result', img_result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()