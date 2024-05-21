import cv2
import datetime
#mediapipe

import mediapipe as mp




webcam = cv2.VideoCapture(0)
#webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#webcam.set(cv2.CAP_PROP_FRAME_HEIGH, 480)

while True:

    ret,frame = webcam.read()
    if ret:


        cv2.putText(frame,str(datetime.datetime.now()),(10,15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
        cv2.imshow("Immagini", frame)

        if cv2.waitKey(1) == 27:
           break

webcam.release()
cv2.destroyAllWindows()
    #ret mi dice se è riuscito a leggere un fotogramma
    #frame è il fotogramma letto
