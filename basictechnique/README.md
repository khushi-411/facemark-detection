## **Basic Techniques**

This part of my repository consits of basic techniques to detect face. It is divided into four parts:

* Detecting facial region(ROI) in rectangular and circular shape **via an Image.**
* **Live detection** of face (both in rectangular and circular shape) using Laptop's webcam.

### **Logic**

* In this project pre-trained **haarcascades** models are used to detect ROI. 
* By default **detectMultiscale()** outputs ROI as a list of rectangles.
* To detect face in circular shape, I found center and raidus from the detected rectangles.

### **Output**

https://github.com/khushi-411/Play-With-Faces/issues/1#issue-815163067
