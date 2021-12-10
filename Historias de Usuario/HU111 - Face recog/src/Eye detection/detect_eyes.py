import cv2, os


#face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface_improved.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
eye_cascade = cv2.CascadeClassifier('model.h5')
cap = cv2.VideoCapture(0)

while True:
    # Guardo el frame actual en img
    _, img = cap.read()

    # Convierto a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecta ojos
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
    # Detecta caras
    # faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Guardo los 2 primeros ojos
    eye = eyes[0:2]


    # Dibujo un circulo para cada ojo
    for (x, y, w, h) in eye:
        if len(eye) == 2:
            os.system('cls')
            print(eye[0])
            print(eye[1])
        
        cv2.circle(img, (x+int(w/2), y+int(h/2)), int(w/2), (255, 0, 0), 2)

    #for (x, y, w, h) in faces:

        #cv2.rectangle(img, (x, y), (x+w, y+h),(255, 0, 0), 2)
        
    # Muestra el frame 
    cv2.imshow('facial eye detector', img)

    # esc para frenar 
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()