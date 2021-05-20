import cv2
import sys

#get user supplied values
imagePath = sys.argv[1]
cascPath = sys.argv[2]

#creating the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

#Reading the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#detect faces in the image
#Need to experiment with window size, scale factor, etc. These are just common ones
faces = faceCascade.detectMultiScale(gray, scaleFactor= 1.3, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)

print("Found {0} faces!".format(len(faces)))

#Draw a rectangle around the faces
for(x, y, w, h) in faces:
    cv2.rectangle(image,(x, y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
