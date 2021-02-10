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

def _drawFace(face):
    
    # Accessing points
    top_left_xpoint = face[0]
    top_left_ypoint = face[1]
    width = face[2]
    height = face[3]
        
    # calculate center and radius
    center = [top_left_xpoint + int(width/2), top_left_ypoint + int(height/2)]
    radius = max(int(width/2), int(height/2))
        
    cv2.circle(img, (center[0], center[1]), radius, (255, 255, 255), 3)
    
    return img

def _drawEye(eye):
    
    # Accessing points
    top_left_xpoint = eye[0]
    top_left_ypoint = eye[1]
    width = eye[2]
    height = eye[3]
        
    # calculate center and radius
    center = [top_left_xpoint + int(width/2), top_left_ypoint + int(height/2)]
    radius = max(int(width/2), int(height/2))
        
    cv2.circle(img, (center[0], center[1]), radius, (255, 255, 255), 3)
    
    return img

if __name__ == "__main__":
    
    # Loading image
    if len(sys.argv) < 1:
        img_path = sys.argv[1]
    else:
        img_path = "TaylorSwift.jpg"
    
    # Reading image
    img = cv2.imread(img_path, 1)
    
    # Resize image
    img = cv2.resize(img, (500, 740))
    
    begin = time.time()
    
    # Loading haarcascades to detect face and eyes
    faces = _detectFace(img)
    eyes = _detectEyes(img)
    
    if len(faces) == 0:
        print("No face detected")
        sys.exit(0)
    
    # Drawing circle around face
    for face in faces:
        _drawFace(face)
        
    # Drawing circle around eye
    for eye in eyes:
        _drawEye(eye)
    
    #time.sleep(1)
    end = time.time()
    print("Time taken : ", end-begin)
    
    # Display image    
    cv2.imshow("Image", img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
