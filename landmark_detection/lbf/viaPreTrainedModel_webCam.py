import cv2, sys, time

if __name__ == "__main__":
    
    if len(sys.argv) < 1:
        img_path = sys.argv[1]
    else:
        # Capturing video frame
        video_cap = cv2.VideoCapture(0)
        
    # To change the shape of video frame
    video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
    video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
        
    # Loading trained frontal face classifier 
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    # Through lbf model
    facemark = cv2.face.createFacemarkLBF()
    facemark.loadModel("lbfmodel.yaml")
    
    while True:
        
        # Reading frame
        ret, frame = video_cap.read()
        
        if ret:
        
             # To change colored image to gray scale
            if len(frame.shape) != 1:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            faces = face_cascade.detectMultiScale(gray, 1.1, 5)
            
            if len(faces) > 0:
                
                start = time.time()
                ret_val, landmarks = facemark.fit(frame, faces)
                print("Time taken to fit face : ", time.time() - start)
                
                for i in range(len(landmarks)):
                    cv2.face.drawFacemarks(frame, landmarks[i])
                    
            else:
                print("No Face Detected")
    
            cv2.imshow("Frame", frame)
            out.write(frame)
            if cv2.waitKey(5) == ord('q'):
                break
        else:
            break
    
    video_cap.release()
    out.release()
    cv2.destroyAllWindows()
