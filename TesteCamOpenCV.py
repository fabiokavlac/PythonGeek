import cv2
import time

cap = cv2.VideoCapture(0)

while True:
    time.sleep(1) # adiciona um atraso de 1 segundo
    ret, frame = cap.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

