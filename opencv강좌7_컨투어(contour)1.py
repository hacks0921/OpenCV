import cv2 as cv

# 1) 이미지 읽기
# 2) Gary 변환  (회색)
# 3) Binary 변화(흰색,검정색)
# 4) 컨투어 검출

img_color = cv.imread('test.PNG')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 128, 255, 0)
print(ret) # 임계값

# 컨투어 검출 함수
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)   # 꼭지점만 선택 가로/세로
# contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)   # 전체를 다 ~ 선택
# cv.drawContours(img_color, contours, 0, (255, 0, 0), 3)  # 모든 컨투어 그리기

for cnt in contours:
    print(cnt)
    for p in cnt:
        print(p)
        cv.circle(img_color, (p[0][0], p[0][1]), 3, (255,0,0), -1)
# cv.drawContours(img_color, contours, 1, (0, 255, 0), 3)  # 이미지 위에 그림을 그린다

cv.imshow("result", img_color)
cv.waitKey(0)


#image , mode , method ,[contours[,hierarchy[,offset]]])
# cv.CHAIN_APPROX_NONE : 전체
# cv.CHAIN_APPROX_SIMPLE: 꼭지점 선택

#cv.RETR_LIST : 리트리버 모드
# 1. RETR_TREE : 모든 리스트를 표시 한다, 외부 부모, 내부 자식 ... 순서로
# 2. RETR_LIST : 계측적 특성이 필요 없는 경우 사용
# 3. RETR_EXTERNAL : 가장 외부 컨투어만  표시
# 4. RETR_CCOMP : 외부 레벨 1, 내부 레벨 2