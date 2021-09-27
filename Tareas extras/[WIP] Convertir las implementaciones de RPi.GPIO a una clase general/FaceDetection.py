from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2

def eye_aspect_ratio(eye) -> float:
    '''Devuelve la relacion de aspecto del ojo ingresado'''
    A = dist.euclidean(eye[1], eye[5])                                      # Saco distancias entre los puntos invertidos de un ojo (distancia euclidiana)
    B = dist.euclidean(eye[2], eye[4])
    
    C = dist.euclidean(eye[0], eye[3])
    
    relacion = (A+B)/(C*2)                                                  # Saco la relacion de h/w (Cabe aclarar que A y B geneneralmente tiene el mismo valor y por eso se multiplica por 2 a C)
    return relacion

def mouth_aspect_ratio(mouth) -> float:
    '''Devuelve la relacion de aspecto de la boca'''
    A  = dist.euclidean(mouth[2], mouth[12])
    B = dist.euclidean(mouth[4], mouth[8])
    
    C = dist.euclidean(mouth[0], mouth[6])
    relacion = (A+B)/(C*2)
    return relacion
    
 
detector = dlib.get_frontal_face_detector()                                
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  

leftStart, leftEnd = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"] 
rightStart, rightEnd = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

mouthStart, mouthEnd = face_utils.FACIAL_LANDMARKS_IDXS["mouth"] 

videoSource = VideoStream(src=0).start() 

def detectClosedEyesAndMouth():
    counter = 0 

    eyeRelationThreshold = 0.20                                   
    mouthRelationThreshold = 0.44                                             
    maxConsecutiveFrames = 2    

    while 1:
        frame = videoSource.read()
        #frame = imutils.resize(frame, width=1000)
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

        faces = detector(grayFrame, 0)

        for face in faces: 
            shape = predictor(grayFrame, face) 
            shape = face_utils.shape_to_np(shape) 

            leftEye = shape[leftStart:leftEnd] 
            rightEye = shape[rightStart:rightEnd]   
            mouth = shape[mouthStart:mouthEnd]


            leftEAR = eye_aspect_ratio(leftEye) 
            rightEAR = eye_aspect_ratio(rightEye)
            eyesEAR = (leftEAR+rightEAR)/2

            mouthEAR = mouth_aspect_ratio(mouth)

        
            if eyesEAR < eyeRelationThreshold and mouthEAR < mouthRelationThreshold:
                counter += 1
            else:            
                counter = 0 
            
            if counter >= maxConsecutiveFrames: 
                videoSource.stop()    
                return       