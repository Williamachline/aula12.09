import cv2
img = cv2.imread("aula12.09/poyo.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("maindenless", img)
cv2.imshow("cinza", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()