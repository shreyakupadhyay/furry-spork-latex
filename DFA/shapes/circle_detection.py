# Circle Detection

import cv2
import sys
import numpy as np

def DetectCircles(image):
    minpercent = 0.13
    maxpercent = 0.33
    height,width = image.shape[:2]
    minValue = min(height,width)
    maxValue = max(height,width)
    min_radius = int(minpercent * minValue/2)
    max_radius = int(maxpercent * maxValue/2)
    houghcircles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=min_radius,maxRadius=max_radius)
    houghcircles = np.uint16(np.around(houghcircles))
    return houghcircles

def test():
    img = cv2.imread(sys.argv[1],0)
    for i in DetectCircles(img)[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    cv2.imshow('detected circles',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test()
