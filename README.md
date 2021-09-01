## Facial Landmark Detection

Thanks to [Kushashwa Ravi Shrimali](https://github.com/krshrimali) for inspiring me and mentoring me throughout this project. 

### Aim & Structure of Repo
- basictechnique/
  - Aim 1: To detect faces for both in images and via using webcam for real time detection.
  - Aim 2: Improve the accuracy of detection model (Cropped the facial region in circular shape.
- data/
  - Haarcascade files for frontal face, mouth, nose and eyes.
- filter1/
  - `messyBoxes.py:` Blackens the mouth and eyes region and Blurs the background.
  - `invisibilityCloak.py`: Objects with red color becomes invisible in half of the screen. 
  - `putStickers.py`: Puts glasses and mustache as facial spaces.
  - `makeCartoon.py`: Cartoonify images.
- landmark_detection/
  - `aam/`: TODO
  - `kazemi/preTrained_image.py` && `kazemi/viaPreTrainedModel_webCam.py`: Detects facial points both for images and via using webcam.
  - `lbf/preTrained_image.py` && `viaPreTrainedModel_webCam.py`: Detects facial points both for images and via using webcam.

#### To Clone the repository, run:
```
git clone https://github.com/khushi-411/facemark-detection
```

#### Dependencies
- `opencv`
- `opencv_contrib`
