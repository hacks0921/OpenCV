import cv2

#더미 함수를 생성한다
def nothing(x):
    pass

# Trackbar 추가
cv2.namedWindow("Binary")  # 윈도우 이름 설정
cv2.createTrackbar("threshold", "Binary", 0,255, nothing)  # 식별자 이름 / 윈도우 이름 / Min / MAX /
cv2.setTrackbarPos("threshold", "Binary", 127) # 초기값 127 설정

img_color = cv2.imread('img.jpg', cv2.IMREAD_COLOR)
cv2.imshow("Color", img_color)
# cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", img_gray)
# cv2.waitKey(0)

# ★★★★★★★바이너리 이미지 생성★★★★★★
# 그레이 이미지, 기준값(127), 변경할 값(255), 바이너리
while(True):
    low = cv2.getTrackbarPos("threshold", "Binary")  # Trackbar에서 현재 최소값 가지고 오기
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY)
    cv2.imshow("Binary", img_binary)
    if cv2.waitKey(1)&0xFF == 27:  # ESC 누르면 빠져나옴
        break
cv2.destroyAllWindows()

# def nothing(x):
#     pass
# cv2.namedWindow('Binary')
# cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)
# cv2.setTrackbarPos('threshold', 'Binary', 127)
# img_color = cv2.imread('red_ball.jpg', cv2.IMREAD_COLOR)
# cv2.imshow('Color', img_color)
# img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray', img_gray)
#
# while(True):
#     low = cv2.getTrackbarPos('threshold', 'Binary')
#     ret,img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY_INV)
#     cv2.imshow('Binary', img_binary)
#     img_result = cv2.bitwise_and(img_color, img_color, mask = img_binary)
#     cv2.imshow('Result', img_result)
#     if cv2.waitKey(1)&0xFF == 27:
#         break
# cv2.destroyAllWindows()