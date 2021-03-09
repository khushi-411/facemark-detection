# **Cartoonify Image**

This is a simple filter designed via OpenCV which cartoonify images (top to down). As the window slides from top of the image, the portion cartoonifies.

## **Task**

* Highlight edges.
* Reduce color.

## **Steps**

* Find edges.
* Reduce noise (for better results).
* Change RGB image to color painting.
* Mix edges and color image into single image.
* Replace cartoon image with normal as the line moves top to bottom.

## **Uniqueness**

* Demostrate four different concepts - Edge detection, Blurring, Thresholding, Bitwise And
* Produces funny output.

## **Output**

We'll get output file saved as *filter4.mp4* 

https://user-images.githubusercontent.com/62256509/110498464-5c72e380-811d-11eb-97e5-4cacdce8d6fb.mp4

These are the screenshots of my output:

* **Original Image**

![Screenshot (49)](https://user-images.githubusercontent.com/62256509/110502148-f1c3a700-8120-11eb-9e6f-c8559bd22669.png)

* **At 11th seconds**

![Screenshot (50)](https://user-images.githubusercontent.com/62256509/110502384-29325380-8121-11eb-8f7f-c8031d3bee4f.png)

* **At Last-24th second**

![Screenshot (51)](https://user-images.githubusercontent.com/62256509/110502545-4cf59980-8121-11eb-82c1-be6959f6fa1d.png)

## **Reference**

* http://datahacker.rs/002-opencv-projects-how-to-cartoonize-an-image-with-opencv-in-python/
