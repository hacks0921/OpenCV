import cv2 as cv

# 1) 이미지 읽기
# 2) Gary 변환  (회색)
# 3) Binary 변화(흰색,검정색)
# 4) 컨투어 검출

img_color = cv.imread('contour.PNG')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 128, 255, 0)
print(ret) # 임계값

# 컨투어 검출 함수
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img_color, contours, 0, (255, 0, 0), 3)  # 모든 컨투어 그리기
cv.drawContours(img_color, contours, 1, (0, 255, 0), 3)  # 이미지 위에 그림을 그린다
cv.drawContours(img_color, contours, -1, (50, 155, 110), 3)  # 이미지 위에 그림을 그린다

cv.imshow("result", img_color)
cv.waitKey(0)
