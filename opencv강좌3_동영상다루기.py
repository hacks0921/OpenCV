import cv2
#★★★★★★★★★★★ 1장의 이미지를 캡춰하기★★★★★★★★★★
# cap = cv2.VideoCapture(0)
# ret,img_color = cap.read()
# cv2.imshow("color", img_color)  # 1장의 이미지를 읽는다
# cv2.waitKey(0)
# cap.release()
# cv2.destroyAllWindows()
#★★★★★★★★★★★ 동영상 캡춰하기★★★★★★★★★★
# cap = cv2.VideoCapture(0)
# while True:
#     ret, img_color = cap.read()
#     if ret == False :  # 캡춰가 안되는 경우 다시 처음부터 실행 문
#         continue
#     img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("Color", img_color)
#     cv2.imshow("Gray", img_gray)
#     if cv2.waitKey(1)&0xFF == 27 :  # 1초 대기후에 다음 구분 실행 # ESC = 27번
#         break
# cap.release()
# cv2.destroyAllWindows()
#★★★★★★★★★★★ 동영상 저장하기 ★★★★★★★★★★

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))
# 초당 프래임수 , 저장할 영상의 크기

while True:
    ret, img_color = cap.read()
    if ret == False :  # 캡춰가 안되는 경우 다시 처음부터 실행 문
        continue
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Color", img_color)
    cv2.imshow("Gray", img_gray)
    if cv2.waitKey(1)&0xFF == 27 :  # 1초 대기후에 다음 구분 실행 # ESC = 27번
        break
cap.release()
writer.release()
cv2.destroyAllWindows()