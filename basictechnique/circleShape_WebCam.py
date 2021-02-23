import cv2, sys, time

def _detectFace(img):
    
    # Convert to gray scale
    if len(img.shape) != 1:
        image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Loading trained frontal face classifier 
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    # Detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles.
    faces = face_classifier.detectMultiScale(image, 1.1, 5)
    
    return faces

def _detectEyes(img):
    
    # Convert to gray scale
    if len(img.shape) != 1:
        image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Loading trained frontal face classifier 
    eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')
    
    # Detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles.
    eyes = eye_classifier.detectMultiScale(image, 1.1, 5)
    
    return eyes

def _drawFace(face, frame):
    
    # Accessing points
    top_left_xpoint = face[0]
    top_left_ypoint = face[1]
    width = face[2]
    height = face[3]
        
    # calculate center and radius
    center = [top_left_xpoint + int(width/2), top_left_ypoint + int(height/2)]
    radius = max(int(width/2), int(height/2))
        
    frame = cv2.circle(frame, (center[0], center[1]), radius, (255, 255, 255), 3)
    
    return frame

def _drawEye(eye, frame):
    
    # Accessing points
    top_left_xpoint = eye[0]
    top_left_ypoint = eye[1]
    width = eye[2]
    height = eye[3]
        
    # calculate center and radius
    center = [top_left_xpoint + int(width/2), top_left_ypoint + int(height/2)]
    radius = max(int(width/2), int(height/2))
        
    frame = cv2.circle(frame, (center[0], center[1]), radius, (255, 255, 255), 3)
    
    return frame

if __name__ == "__main__":
    
    # Capturing video frame
    video_cap = cv2.VideoCapture(0)
        
    # To change the shape of video frame
    video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
    video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('rect.mp4', fourcc, 20.0, (640,  480))
    
    while True:
        
        ret, frame = video_cap.read()
        
        if ret:
            # Loading haarcascades to detect face and eyes
            faces = _detectFace(frame)
            eyes = _detectEyes(frame)
    
            # Drawing circle around face if found
            if len(faces) != 0:
                for face in faces:
                    _drawFace(face, frame)
                cv2.putText(frame, 'Face Detected', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
            else:
                cv2.putText(frame, 'Face Not Detected', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
        
            # Drawing circle around eye if found
            if len(eyes) != 0:
                for eye in eyes:
                    _drawEye(eye, frame)
                cv2.putText(frame, 'Eyes Detected', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
            else:
                cv2.putText(frame, 'Eyes Not Detected', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
         
            # Display video   
            cv2.imshow("Frame", frame)
            out.write(frame)
            if cv2.waitKey(5) == ord('q'):
                break
        else:
            break
    
    video_cap.release()
    out.release()
    cv2.destroyAllWindows()
