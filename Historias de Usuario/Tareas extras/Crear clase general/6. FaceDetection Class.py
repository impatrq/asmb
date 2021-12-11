from MainClass import ASMB

asmb = ASMB()
print("Detectando ojos y boca")
fd = asmb.FaceDetection('eyes&Mouth')
fd.detect()
print("Ahora con el barbijo")
fd = asmb.FaceDetection('mask')
fd.detect()