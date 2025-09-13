
import cv2
imagem = cv2.imread("escola2.png")
cv2.imshow("Janela da imagem",imagem)
print("Visão Computacional")
cv2.waitKey(0)
cv2.destroyAllWindows()
Jonathan Bruno Ferreira Barros
21:31
while True:
    ok, frame = cap.read()
    if not ok:
        cap.release()
        raise RuntimeError ("Falha ao carregar o primeiro frame")
        break
    cv2.imshow("Video",frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.waitKey(0)

import cv2
#imagem = cv2.imread("escola2.png")
#cv2.imshow("Janela da imagem",imagem)
#print("Visão Computacional")
#cv2.waitKey(0)
#cv2.destroyAllWindows()
video_path = r'race.mp4'
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise FileNotFoundError(f"Não consegui abrir o vídeo: {video_path}")
while True:
    ok, frame = cap.read()
    if not ok:
        cap.release()
        raise RuntimeError ("Falha ao carregar o primeiro frame")
        break
    cv2.imshow("Video",frame)
if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.waitKey(0)