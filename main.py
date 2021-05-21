import cv2 as cv
import numpy as np

# read image
img = cv.imread('data/8.jpg')

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

r_img = rescaleFrame(img)

cv.imshow('1', r_img)

# simple threshholding
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)
threshold, thresh = cv.threshold(gray, 115, 255, cv.THRESH_BINARY)

r_thresh = rescaleFrame(thresh)
cv.imshow('Simple Thresholded', r_thresh)

# erosion
kernel = np.ones((15,15), np.uint8)
img_dilation = cv.dilate(thresh, kernel, iterations=1)
img_erode = cv.erode(img_dilation,kernel, iterations=1)
# clean all noise after dilatation and erosion
img_erode = cv.medianBlur(img_erode, 7)

r_img_erode = rescaleFrame(img_erode)
cv.imshow("2", r_img_erode)

count, labels = cv.connectedComponents(img_erode)

print('objects number is:', count-1)

#===============


cv.waitKey(0)