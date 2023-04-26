import cv2
import time
import os
import numpy as np
import math

cap = cv2.VideoCapture(0)

# Carrega o classificador Haar Cascade para detecção de rosto
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Carrega a imagem a ser detectada
img = cv2.imread('/home/kberton/PycharmProjects/fabiokavlac/images/EU.jpg')

# Verifica se a imagem foi carregada corretamente
if img is None:
    print('Erro ao carregar imagem')
    exit()

# Converte a imagem para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecta os rostos na imagem usando o classificador Haar Cascade
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Desenha um retângulo em volta de cada rosto detectado
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Mostra a imagem com os rostos detectados
cv2.imshow('Imagem', img)
cv2.waitKey(0)

# Fecha todas as janelas
cv2.destroyAllWindows()

