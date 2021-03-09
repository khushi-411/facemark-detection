import cv2, time, sys
 
if __name__ == "__main__":
    
    if len(sys.argv) < 0:
        img_path = sys.argv[1]
    else:
        img_path = "cinderella.jpg"
        
    img = cv2.imread(img_path)
    
    # Resize image
    img = cv2.resize(img, (500, 740))
    
    # To save video
    out = cv2.VideoWriter("filter4.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (img.shape[1], img.shape[0]))
    
    # For cartoon
    edges = cv2.Canny(img, 100, 200)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)
    
    color = cv2.bilateralFilter(img, d=9, sigmaColor=200,sigmaSpace=200)
    
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    # Replacing normal image with cartoon
    for i in range(0, img.shape[0]):
        if i != 0:
            #img[0:cartoon.shape[0], 0:i] = cartoon[0:cartoon.shape[0], 0:i]       # for left to right
            img[0:i, 0:cartoon.shape[1]] = cartoon[0:i, 0:cartoon.shape[1]]        # top to bottom cartoonization
    
        cv2.imshow("Filtered Image", img)
        out.write(img)
        if cv2.waitKey(5) == ord('q'):
            break
    
cv2.destroyAllWindows()
