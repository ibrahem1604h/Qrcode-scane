import cv2
from pyzbar import pyzbar
import webbrowser

#url="http://192.168.70.186:8080/video"
came=cv2.VideoCapture(0)

def Qr(frame):
    code=pyzbar.decode(frame)
    for B in code:
        x,y,w,h=B.rect
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        dat=B.data.decode("utf-8")
        type=B.type
        
        if dat.startswith("WIFI"):
           password= dat.split("P:")[1].split(";")[0]
           print(F"password= {password}") 
        else:  
            print(f"data: {dat}  type: {type}")
        
        
        
        if dat.startswith("http"):
            
            webbrowser.open(dat)
        
    return frame

            
if not came.isOpened:
    print("EROOR")
    exit()
    
    
    
while True:
    ret, frame=came.read()
    if not ret:
       print("error")
       break

    frame=Qr(frame)

    cv2.imshow('cameRa',frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
came.release()
cv2.destroyAllWindows()
   