import cv2, sys

if __name__ == "__main__":
    
    # Reading Images
    img_path = sys.argv[1] if len(sys.argv) < 1 else r"C:\Users\91939\Downloads\cris.jpg"     
    img = cv2.imread(img_path)
        
    glass_path = sys.argv[1] if len(sys.argv) < 1 else r"C:\Users\91939\Downloads\glasses (1).png"
    glass = cv2.imread(glass_path)
    
    mus_path = sys.argv[1] if len(sys.argv) < 1 else r"C:\Users\91939\Downloads\mustache.png"
    mus = cv2.imread(mus_path)
    
    # Loading trained frontal face classifier 
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    if len(img.shape) != 1:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    if len(faces) == 0:
        print("No eyes found")
    else:
        for face in faces:
            
            face_width = face[2] 
            face_height = face[3] 
            
            # For glass
            glass = cv2.resize(glass, (face_width+1, int(0.5 * face_height)+1))
            for i in range(int(0.5 * face_height)+1):
                for j in range(face_width):
                    for k in range(3):
                        if glass[i][j][k] < 255:            
                            img[face[1]+i-int(-0.2*face_height)][face[0]+j][k] = glass[i][j][k]
            
            # For mustache
            mus = cv2.resize(mus, (int(face_width*0.6)+1, int(0.1 * face_height)+1))
            for i in range(int(0.1 * face_height)+1):
                for j in range(int(face_width*0.6)):
                    for k in range(3):
                        if mus[i][j][k] > 0:
                            img[face[1]+i-int(-0.7 * face_height)][int(0.8*face[0])+j+face[0]][k] = mus[i][j][k]
    
    
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
