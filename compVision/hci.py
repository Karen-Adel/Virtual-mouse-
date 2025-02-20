import cv2
import mediapipe as mp
import pyautogui
cap=cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils= mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size() 
index_y=0 

while True:
    st, frame= cap.read()
    frame=cv2.flip(frame,1)  #moving hand in camera in same direction of real hand 1 as in direction of y-axis
    frame_height, frame_width, st= frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgb_frame)  #detect if there is hand
    hands=output.multi_hand_landmarks  
    if hands:
        for hand in hands:  ##for each hand
            drawing_utils.draw_landmarks(frame,hand)  #drawing landmarks on hands
            
            landmarks= hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x* frame_width)  #to move hand in direction of x-axis
                y=int(landmark.y* frame_height)
              #  print(x,y)
                
                if id==8:  #detecting index finger
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    index_x=screen_width/frame_width*x  #mkdar kobr el 4a4a 3n el frame 
                    index_y= screen_height/frame_height*y
                    pyautogui.moveTo(index_x,index_y)  #move mouse cursor with my finger in all screen
                    
                if id==4:  #detecting thumb finger
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    thumb_x=screen_width/frame_width*x  #mkdar kobr el 4a4a 3n el frame 
                    thumb_y= screen_height/frame_height*y
                    print(abs(index_y - thumb_y))
                    
                    if abs(index_y- thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)  #wait one second after click
    cv2.imshow("Mouse", frame)
    if cv2.waitKey(1) & 0xff == ord("x"):
        break

cap.release()   # a2fel el camera el mnwra fo2
cv2.destroyAllWindows()  