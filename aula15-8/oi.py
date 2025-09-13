import cv2
import numpy as np

canvas = np.ones((400,400,3), dtype=np.uint8) * 110

canvas[:] = (200,100,0)
cv2.circle(canvas,(100,100),70,(0,255,255),-1)
cv2.circle(canvas,(300,100),70,(0,255,255),-1)
cv2.circle(canvas,(200,200),100,(0,255,255),-1)


cv2.circle(canvas,(300,100),50,(0,0,255),-1)
cv2.circle(canvas,(100,100),50,(0,0,255),-1)


cv2.circle(canvas,(200,200),80,(0,0,255),-1)

cv2.circle(canvas,(160,195),30,(0,0,0),-1)
cv2.circle(canvas,(230,195),30,(0,0,0),-1)
cv2.circle(canvas,(160,195),5,(255,255,255),-1)
cv2.circle(canvas,(230,195),5,(255,255,255),-1)
cv2.circle(canvas,(200,250),5,(0,255,255),-1)
cv2.circle(canvas,(200,250),3,(255,255,255),-1)





cv2.imshow("Canvas", canvas)   
cv2.waitKey(0)                 
 