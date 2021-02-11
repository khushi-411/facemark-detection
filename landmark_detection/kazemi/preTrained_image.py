import cv2, sys, time

if __name__ == "__main__":
    
    if len(sys.argv) < 0:
        img_path = sys.argv[1]
    else:
        img_path = "TaylorSwift.jpg"
        
    img = cv2.imread(img_path)
    
    # Resize image
    img = cv2.resize(img, (500, 740))
    
    # Convert to gray scale
    if len(img) > 1:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    facemark = cv2.face.createFacemarkKazemi()
    facemark.loadModel("face_landmark_model.dat")
    
    begin = time.time()
    ret_val, landmarks = facemark.fit(gray, faces)
    print("Time taken : ", time.time())
    
    for landmark in landmarks:
        for index, point in enumerate(landmark[0]):
            x_cord = point[0]
            y_cord = point[1]
            cv2.circle(img, (x_cord, y_cord), 1, (255, 255, 255), 1)
            
    #for i in range(len(landmarks)):
    #    cv2.face.drawFacemarks(img, landmarks[i])
    
    cv2.imshow("Image", img)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
