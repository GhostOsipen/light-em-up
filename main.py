import cv2 as cv
import numpy

#read image
img = cv.imread('data/1.jpg')

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Cat', resized_image)

cv.waitKey(0)