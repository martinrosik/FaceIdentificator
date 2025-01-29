import cv2
import numpy as np

web_cam = cv2.VideoCapture(0)

frame_width = int(web_cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(web_cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') 
left_eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_lefteye_2splits.xml')
right_eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_righteye_2splits.xml') 
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml') 



def detect(gray, frame): 
    font = cv2.FONT_HERSHEY_DUPLEX
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    left_eye = left_eye_cascade.detectMultiScale(gray, 1.8, 20)
    right_eye = right_eye_cascade.detectMultiScale(gray, 1.8, 20)

    for (x, y, w, h) in faces: 
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        cv2.putText(frame, "Face", (x, y-10), font, 0.6, (255, 0, 0), 2) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = frame[y:y + h, x:x + w] 
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)


        for (sx, sy, sw, sh) in smiles: 
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (124,252,0), 2) 
            cv2.putText(roi_color, "Smile", (sx, sy-5), font, 0.6, (124, 252, 0), 2)

        for (lex, ley, lew, leh) in left_eye: 
            cv2.rectangle(frame, (lex, ley), ((lex + lew), (ley + leh)), (0, 0, 255), 2)
            cv2.putText(frame, "Left Eye", (lex, ley-5), font, 0.6, (0, 0, 255), 2)

        for (rex, rey, rew, reh) in right_eye: 
            cv2.rectangle(frame, (rex, rey), ((rex + rew), (rey + reh)), (0, 0, 255), 2)
            cv2.putText(frame, "Right Eye", (rex, rey-5), font, 0.6, (0, 0, 255), 2)
    return frame 

while web_cam.isOpened():
    _, frame = web_cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
    
    canvas = detect(gray, frame)    

    cv2.imshow('Face Indentificator', canvas)

    if cv2.waitKey(1) == ord('q'):
        break

web_cam.release()
cv2.destroyAllWindows()