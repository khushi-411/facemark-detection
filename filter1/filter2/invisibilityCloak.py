import cv2, sys, time
import numpy as np

if __name__ == "__main__":
    
    # Capturing video
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    
    # For saving
    out = cv2.VideoWriter("filter2.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (frame.shape[1], frame.shape[0]))
    
    #print(frame.shape[0])
    #print(frame.shape[1])
    
    # Capturing background
    background = 0
    
    for i in range(60):
        ret,background = cap.read()
        background = background[0:640, 0:290]
    
    while True:    
        ret, frame = cap.read()
        
        if not ret:
            break  
        
        frame = cv2.flip(frame, 1) 
            
        #cv2.line(frame, (290, 0), (290, 640), (0, 0, 0), thickness = 2) 
        
        _frame = frame[0:640, 0:290]
        
        hsv = cv2.cvtColor(_frame, cv2.COLOR_BGR2HSV)
        
        # Generating mask to detect red color
        
        lower_red = np.array([0,120,70])
        upper_red = np.array([10,255,255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        lower_red = np.array([170,120,70])
        upper_red = np.array([180,255,255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)
        
        mask1 = mask1 + mask2
        
        # Refining the mask corresponding to the detected red color
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=2)
        mask1 = cv2.dilate(mask1, np.ones((3,3), np.uint8), iterations = 1)
        mask2 = cv2.bitwise_not(mask1)
        
        # Generating the final output
        res1 = cv2.bitwise_and(background, background, mask=mask1)
        res2 = cv2.bitwise_and(_frame, _frame, mask=mask2)
        final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
        
        # Replacing with original image
        frame[0:640, 0:290] = final_output
        
        cv2.imshow("Frame", frame)
        
        if cv2.waitKey(5) == ord('q'):
            break
        out.write(frame)
        
    cap.release()
    cv2.destroyAllWindows()
