import cv2
import numpy as np
import os

path = os.path.dirname(os.getcwd())

# Trained haar cascade for objects o be identified
filename = path+'\\Data-Science-Projects\\Object_detection_image\\mydetector.xml'

# Load the face cascade file
face_cascade = cv2.CascadeClassifier(filename)

# Check if the face cascade file has been loaded
if face_cascade.empty():
  raise IOError('Unable to load the face cascade classifier xml file')

# Define the scaling factor
scaling_factor = 0.5

# Select image for testing.
filepath = path+'\\Data-Science-Projects\\Object_detection_image\\images\\test\\1a.bmp'

# Read image for test
image = cv2.imread(filepath, 0)

cv2.imshow("Input Image", image)

frame = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor,  interpolation=cv2.INTER_AREA)

 # Run the face detector on the grayscale image
rects = face_cascade.detectMultiScale(frame)

# Draw rectangles on the image
for (x,y,w,h) in rects:
     cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

# Display the image
cv2.imshow('Face Detector', frame)

# Check if Esc key has been pressed
cv2.waitKey(0)
cv2.destroyAllWindows()

