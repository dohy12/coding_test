import cv2

img = cv2.imread('./bugger.png')
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 결과 출력
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()