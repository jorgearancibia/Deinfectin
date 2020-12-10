"""
Este es un script para adquirir imágenes utilizando la web cam del 
pc con la librería open cv de python en el proyecto "Desinfectín" de
Robótica
"""


import cv2
import numpy as np
    
# inicializar capturadora de imagen (webcam)
cam = cv2.VideoCapture(0)


# loop para tomar frames continuamente con la capturadora
while True:
    
    # obtener frame de la capturadora
    _, frame  = cam.read()
    
    # redimensionar a una imagen de 360x480
    frame = cv2.resize(frame, (1080, 720))
    frame = cv2.flip(frame, 1)
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', img_gray)

    if cv2.waitKey(1) == 27:
        break
    
# libera la capturadora una vez ejecutado el programa 
cam.release()
cv2.destroyAllWindows()