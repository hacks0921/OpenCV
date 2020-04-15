import cv2

img_color = cv2.imread('img.jpg', cv2.IMREAD_COLOR)
cv2.namedWindow("Show Image")
cv2.imshow("Show Image", img_color) # Show Image 윈도우 창에 그려준다
cv2.waitKey(0)  # 특정 키보드 입력 받을떄 까지 대기

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imshow("Show Image", img_gray)
cv2.waitKey(0)
cv2.imwrite('save_gray_image.jpg', img_gray)
cv2.destroyAllWindows() # 자원 해제