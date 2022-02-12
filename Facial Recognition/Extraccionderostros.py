import cv2
import os
import imutils

def extraccionDeRostros(personName):    
    if not os.path.exists('Rostros encontrados'):
        print('Carpeta creada: Rostros encontrados')
        os.makedirs('Rostros encontrados')
        
        
    dataPath = 'C:\Jeison\Python\RECONOCIMIENTO FACIAL\Data'#Cambia a la ruta donde hayas almacenado Data
    personPath = dataPath + '/' + personName
    
    if not os.path.exists(personPath):
        print('Carpeta creada: ',personPath)
        os.makedirs(personPath)
        
       
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    
    #cap = cv2.VideoCapture('ATM1.mp4')
    
    faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    count = 0   
    
    while True:
        
        ret, frame = cap.read()
        
        if ret == False: 
            
            print ('me sali en count :' ,count)
            break
        
        frame =  imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        
        for (x,y,w,h) in faces:
            print(count)
        
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            
            #Escribo en carpeta el cuadro sacado
            cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
            
            count = count + 1
            
        #abre el framework view    
        cv2.imshow('frame',frame)
        
        
        
        k =  cv2.waitKey(1)
        
        if k == 27 or count >= 500:
            
            break
        
    cap.release()
    cv2.destroyAllWindows()
    

extraccionDeRostros('JeisonB')