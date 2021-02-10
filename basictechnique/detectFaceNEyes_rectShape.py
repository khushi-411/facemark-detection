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

if __name__ == "__main__":
    
    # Loading image
    if len(sys.argv) < 1:
        img_path = sys.argv[1]
    else:
        img_path = "TaylorSwift.jpg"
    
    # Reading image
    img = cv2.imread(img_path, 1)
    
    img = cv2.resize(img, (500, 740))
    
    begin = time.time()
    
    faces = _detectFace(img)
    #eyes = _detectEyes(img)
    
    # Drawing rectangle around face
    for face in faces:
        cv2.rectangle(img, (face[0], face[1]), (face[0]+face[2], face[1]+face[3]), (255, 255, 255), 2)
        
    # Drawing rectangle around eye
    for eye in eyes:
        cv2.rectangle(img, (eye[0], eye[1]), (eye[0]+eye[2], eye[1]+eye[3]), (255, 255, 255), 2)
    
    # time.sleep(1)
    end = time.time()
    print("Time taken : ", end-begin)
    
    # Display image    
    cv2.imshow("Image", img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
