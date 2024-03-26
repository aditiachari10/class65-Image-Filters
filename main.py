import cv2

path = 'lion.png'
originalImage=cv2.imread(path)
originalImage=cv2.resize(originalImage,(500,500))
# rgb is not a readable sequence    reads bgR sequence

#grayImage
grayscaleImage= cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
oilPaintImage= cv2.xphoto.oilPainting(originalImage, size=4, dynRatio=10)


invertedImage= 255-grayscaleImage
blurredImage=cv2.GaussianBlur(invertedImage, (21,21), 0)
sketchImage= cv2.divide(grayscaleImage, 255-blurredImage, scale=256)
cv2.imshow('origin', originalImage)
cv2.imshow('grayImage', grayscaleImage)
cv2.imshow('invertedImage', invertedImage)
cv2.imshow('blurredImage', blurredImage)
cv2.imshow('oilImage', oilPaintImage)
cv2.imshow('sketchImage', sketchImage)

cv2.imwrite('sketch.png', sketchImage)
cv2.waitKey(0)