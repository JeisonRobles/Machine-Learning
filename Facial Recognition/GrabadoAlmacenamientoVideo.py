import cv2
import Extraccionderostros as Ex


import cv2
import os
import imutils
import numpy as np


Nombre = input('escriba su nombre  =     ')



def Grabar(Nombre):
    
    Nombre = Nombre + '.mp4'
    captura = cv2.VideoCapture(0)
    
    
    
    salida = cv2.VideoWriter(Nombre,cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
    
    while (captura.isOpened()):
        
      ret, imagen = captura.read()
      
      if ret == True:
          
        cv2.imshow('video', imagen)
        salida.write(imagen)
       
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            
          break
      
      else: break
    
    captura.release()
    salida.release()
    cv2.destroyAllWindows()












def extraccionDeRostros(personName): 
    
    if not os.path.exists('Rostros encontrados'):
        print('Carpeta creada: Rostros encontrados')
        os.makedirs('Rostros encontrados')
        
    
    #personName = 'Jeison'
    
    dataPath = 'C:\Jeison\Python\RECONOCIMIENTO FACIAL\Data'#Cambia a la ruta donde hayas almacenado Data
    personPath = dataPath + '/' + personName
    
    
    
    if not os.path.exists(personPath):
        print('Carpeta creada: ',personPath)
        os.makedirs(personPath)
        
       
        
    #cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    
    cap = cv2.VideoCapture(personName+'.mp4')
    
    
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
            print('LEYENTO DEL FOTOGRAMA NUMERO = ',count)
        
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            
            #Escribo en carpeta el cuadro sacado
            cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
            
            count = count + 1
            
        #abre el framework view    
        cv2.imshow('frame',frame)
        
        
        
        k =  cv2.waitKey(1)
        
        if k == 27 or count >= 1500:
            
            break
        
      
    cap.release()
    cv2.destroyAllWindows()
    
    




def entrenador():

    dataPath = 'C:\Jeison\Python\RECONOCIMIENTO FACIAL\Data'#Cambia a la ruta donde hayas almacenado Data
    peopleList = os.listdir(dataPath)
    
    
    print('Lista de personas: ', peopleList)
    
    labels = []
    facesData = []
    label = 0
    for nameDir in peopleList:
        personPath = dataPath + '/' + nameDir
        print('Leyendo las imágenes')
        for fileName in os.listdir(personPath):
            print('Rostros: ', nameDir + '/' + fileName)
            labels.append(label)
            facesData.append(cv2.imread(personPath+'/'+fileName,0))
            # image = cv2.imread(personPath+'/'+fileName,0)
            # cv2.imshow('image',image)
            #cv2.waitKey(10)
        label = label + 1
    
    
    
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    print("Entrenando...")
    face_recognizer.train(facesData, np.array(labels))
    face_recognizer.write('modeloLBPHFace.xml')
    print("Modelo almacenado...")
    
    
    
    
def Reconocimiento():
    
    
    dataPath = 'C:\Jeison\Python\RECONOCIMIENTO FACIAL\Data' #Cambia a la ruta donde hayas almacenado Data
    imagePaths = os.listdir(dataPath)
    
    print('imagePaths=',imagePaths)
    #face_recognizer = cv2.face.EigenFaceRecognizer_create()
    #face_recognizer = cv2.face.FisherFaceRecognizer_create()
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    
    # Leyendo el modelo
    #face_recognizer.read('modeloEigenFace.xml')
    #face_recognizer.read('modeloFisherFace.xml')
    face_recognizer.read('modeloLBPHFace.xml')
    
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    #cap = cv2.VideoCapture('Video.mp4')
    faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    while True:
        ret,frame = cap.read()
        if ret == False: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)
            cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
            '''
            # EigenFaces
            if result[1] < 5700:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
            
            # FisherFace
            if result[1] < 500:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
            '''
            
            # LBPHFace
            if result[1] < 60:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                
            
        cv2.imshow('frame',frame)
        k = cv2.waitKey(1)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()    
    
    
    
   
    
    
    
Grabar(Nombre)
extraccionDeRostros(Nombre)    
entrenador()
Reconocimiento()

