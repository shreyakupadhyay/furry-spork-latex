'''
Description: Using countours for finding the circles.

'''
import cv2
import sys
raw_image = cv2.imread(sys.argv[1])
# cv2.imshow('Original Image', raw_image)
# cv2.waitKey(0)

bilateral_filtered_image = cv2.bilateralFilter(raw_image, 5, 175, 175)
# cv2.imshow('Bilateral', bilateral_filtered_image)
# cv2.waitKey(0)

edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
# cv2.imshow('Edge', edge_detected_image)
# cv2.waitKey(0)

_, contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_list = []
for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    area = cv2.contourArea(contour)
    im = raw_image.copy()
    cv2.drawContours(im, [contour],  -1, (255,0,0), 2)
    cv2.imshow('Objects Detected',im)
    cv2.waitKey(0)
    # if ( (len(approx) > 5) & (len(approx) < 50) & (area > 10) ):
    # # if cv2.isContourConvex(contour):
    #     contour_list.append(contour)
#
# cv2.drawContours(raw_image, contour_list,  -1, (255,0,0), 2)
# cv2.imshow('Objects Detected',raw_image)
cv2.waitKey(0)
