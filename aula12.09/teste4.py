import cv2
import numpy as np

img = np.ones((500, 500, 3), dtype="uint8") * 255

cv2.rectangle(img, (40, 40), (250, 250), (255, 165, 0), -1)
cv2.circle(img, (350, 350), 75, (128, 0, 0), -1)
cv2.line(img, (0, 500), (500, 0), (0, 128, 0), 5)
cv2.putText(img, "William", (180, 260), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)

cv2.imshow("Desenho", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
