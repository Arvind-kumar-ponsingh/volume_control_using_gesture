import cv2
import mediapipe as mp 
import pyautogui 
x1=x2=y1=y2=0
webcam=cv2.VideoCapture(0)
my_hand=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
while True:
    _,img=webcam.read()
    frame_height,frame_width,_ =img.shape
    rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    output=my_hand.process(rgb_img)
    hands=output.multi_hand_landmarks
    if hands:
        for h in hands:
            drawing_utils.draw_landmarks(img,h)
            landmarks = h.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x * frame_width)
                y=int(landmark.y  * frame_height)

                
                if id == 8:
                    cv2.circle(img=img,center=(x,y),radius=10,color=(0,0,0),thickness=3)
                    x1=x
                    y1=y
                if id == 4:
                    cv2.circle(img=img,center=(x,y),radius=10,color=(0,0,0),thickness=3)
                    x2=x
                    y2=y
                else:
                    pass
        dist=((x2-x1)**2+(y2-y1)**2)**(0.5)//4
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),5)
        if dist > 35:
               pyautogui.press("volumeup")
        else:
              pyautogui.press("volumedown")




    cv2.imshow("Volume control using opencv",img)
    key=cv2.waitKey(10)
    if key ==27:
        break
webcam.release()
cv2.destroyAllWindows()
