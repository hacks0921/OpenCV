import cv2

# ■■■■■■■1.이미지 셋팅
src = cv2.imread("images_wedding/src2.jpg", cv2.IMREAD_GRAYSCALE) # 검출하고자 하는 이미지
templit = cv2.imread("images_wedding/wedding_5.jpg", cv2.IMREAD_GRAYSCALE) # 검출 표준 이미지
dst = cv2.imread("images_wedding/wedding_5.jpg")  # 결과 표시 이미지

print(src.shape)
print(templit.shape)
print(dst.shape)

result = cv2.matchTemplate(src, templit, cv2.TM_SQDIFF_NORMED)

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
res = cv2.matchTemplate(templit,src,cv2.TM_SQDIFF_NORMED)

print(minVal)
print(maxVal)

x, y = minLoc
h, w = src.shape

dst = cv2.rectangle(dst, (x, y), (x +  w, y + h) , (0, 0, 255), 1)
# dst = cv2.resize(dst,dsize=(640,480),interpolation=cv2.INTER_AREA)
cv2.namedWindow('Resize Window',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Resize Window',600,800)

cv2.imshow("Resize Window", res)
# cv2.imshow("Resize Window", dst)
# cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
