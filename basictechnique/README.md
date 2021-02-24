## **Basic Techniques**

This part of my repository consits of basic techniques to detect face. It is divided into four parts:

* Detecting facial region(ROI) in rectangular and circular shape **via an Image.**
* **Live detection** of face (both in rectangular and circular shape) using Laptop's webcam.

### **Logic**

* In this project pre-trained **haarcascades** models are used to detect ROI. 
* By default **detectMultiscale()** outputs ROI as a list of rectangles.
* To detect face in circular shape, I found center and raidus from the detected rectangles.

### **Output**

![rectShapeTS](https://user-images.githubusercontent.com/62256509/108959693-c493e500-769a-11eb-8ea7-e8c6bfd3b642.jpeg)

![circleShapeTS](https://user-images.githubusercontent.com/62256509/108959758-de352c80-769a-11eb-80e1-b461cd6ced39.jpeg)
