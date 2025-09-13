import cv2
# Carregar imagem
img = cv2.imread('aula12.09/poyo.jpg')
# Exibir imagem em uma janela
cv2.imshow("tarnished", img)
# Espera até pressionar uma tecla
cv2.waitKey(0)
cv2.destroyAllWindows()