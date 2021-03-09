import cv2, sys

def detect_face(gray):
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_classifier.detectMultiScale(gray, 1.1, 5)
    # If length of faces is 0 return no face found
    if len(faces) == 0:
        print("No faces found")
        return []
    return faces
    
def detect_eyes(gray):
    eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')
    eyes = eye_classifier.detectMultiScale(gray, 1.1, 5)
    # If length of eyes is 0, return not found
    if len(eyes) == 0:
        print("No eyes found")
        return []
    return eyes
    
def detect_mouth(gray):
    mouth_classifier = cv2.CascadeClassifier('mouth.xml')
    mouth = mouth_classifier.detectMultiScale(gray, 1.1, 5)
    # If length of mouth is 0, return not found
    if len(mouth) == 0:
        print("No mouth found")
        return []
    return mouth
    
def blur_img_exceptFace(gray, blur, faces):
    for face in faces:
        # face_img = img[top_left_y:top_left_y+height, top_left_x:top_left_x+width]
        face_img = gray[face[1]:face[1]+face[3], face[0]:face[0]+face[2]]             # Extracting the face part of gray frame to face_img
        blur[face[1]:face[1]+face[3], face[0]:face[0]+face[2]] = face_img             # Replaing blurred part of face with non-blurred(gray scale) image
    return blur
    
 def rep_eyes(blur, canny, eyes):
    for eye in eyes:
        blur[eye[1]:eye[1]+eye[3], eye[0]:eye[0]+eye[2]] = canny[eye[1]:eye[1]+eye[3], eye[0]:eye[0]+eye[2]]           # Replacing the blurred part of eye with canny filter
    return blur
    
def rep_mouth(blur, canny, mouth):
    for mou in mouth:
        blur[mou[1]:mou[1]+mou[3], mou[0]:mou[0]+mou[2]] = canny[mou[1]:mou[1]+mou[3], mou[0]:mou[0]+mou[2]]          # Replacing the blurred part of mouth with canny filter
    return blur
    
def main():
    
    if len(sys.argv) < 1:
        img_path = sys.argv[1]
    else:
        # Capturing video frame
        video_cap = cv2.VideoCapture(0)
    
    while True:
        
        # Reading frame
        ret, frame = video_cap.read()
        # print("Frame Shape : ", frame.shape)          ..... # Frame Shape :  (480, 640, 3)
        
        if ret == False:
            return False
        
        # To change colored image to gray scale
        if len(frame) > 1:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # print("Gray Shape : ", gray.shape)            ...... # Gray Shape :  (480, 640)
        
        # Applying detection models for face, eyes and mouth
        faces = detect_face(gray)
        eyes = detect_eyes(gray)
        mouth = detect_mouth(gray)
        
        # Remove gaussian noise
        blur = cv2.GaussianBlur(gray, (11, 11), 0)
        # print("Blur Shape : ", blur.shape)         ....... # Blur Shape :  (480, 640)  !! When passed gary scale...if frame is passes shape = (480, 640, 3)
        
        # Apping canny edge detector
        canny = cv2.Canny(frame, 100, 200)
        # print("Canny Shape : ", canny.shape)      ........ # Canny Shape :  (480, 640)
        
        blur = blur_img_exceptFace(gray, blur, faces)        # Bluring the whole image except face
        blur = rep_eyes(blur, canny, eyes)                   # Replacing mouth with it's canny filter
        final_output = rep_mouth(blur, canny, mouth)         # Replacing eyes with it's canny filter
        
        cv2.imshow("Final-Output", final_output)
            
        if cv2.waitKey(5) == ord('q'):
            break
            
    video_cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
