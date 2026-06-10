import cv2
#import matplotlib.pyplot as plt
#import numpy as np
#import cv2
from ultralytics import YOLO
#import random
#import EMAILSender
# import os

def startDetection(HOD_name, HOD_mob, Block_Number):
    
    
    model_antiCheating = YOLO("models/AntiCheatingBest.pt","v8") 
    
    
   
    
    # frame=cv2.imread("img1.jpg")
    
    # detect_params=model.predict(frame, conf=0.4, save=False)
    cap = cv2.VideoCapture(2)
    
    
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    count=0 
    imageno=0
    class_list=["Back","Cheat_Exchange","Front","Left","Normal","Null","Right"]
    while True:
        ret, frame = cap.read()
    
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
    
       #print(model.predict("your_image.jpg", confidence=40, overlap=30).json())
        detect_params_cheating = model_antiCheating.predict(source=[frame], conf=0.1, save=False)
        #detect_params_roadhumps = model_roadhump.predict(source=[frame], conf=0.1, save=False)
        
    
      
        for box in detect_params_cheating[0].boxes:
            clsID = box.cls.numpy()[0]
            conf = box.conf.numpy()[0]
            bb = box.xyxy.numpy()[0]
        
            x1 = int(bb[0])
            x2 = int(bb[2])
            y1 = int(bb[1])
            y2 = int(bb[3])
           
            text=class_list[int(clsID)]
            value=round(conf, 3)
            #print("value ",value)
            if(value>0.60 and text!="Normal"):
                disp_text = text+ str(round(conf, 3)) + "%"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(frame, disp_text, (x1, y1), font, 1, (0, 0, 255), 2)
                count=count+1
            
                if count>=5:
                    print("Entered ============")
                    imagepath="Captured_images//"+str(imageno)+".jpg"
                    imageno=imageno+1 
                    cv2.imwrite(imagepath, frame) 
                    
                    import WhatsAppSender
                    WhatsAppSender.sendInfoWA(imagepath,HOD_name, HOD_mob, Block_Number)
                    count=0
                    
    
        
        
        
        if cv2.waitKey(1) == ord('q'):
            break
        cv2.imshow('Anti Cheating Detection System', frame)
            
    
            
    
    # Release the capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

    
# startDetection()                        


        # reciever_email="sukeshinichemate9791@gmail.com"
        # subject="Potholes Alert"
        # body="Dear sir/madam\n There are to many patholes identified in the uploaded video for the concern, please take the action immediately.\n Thank You,\nAutomatic Pothiles Detection System"
        # EMAILSender.sendEmail(reciever_email,subject,body)
    
    
    