# Circle Detection

import cv2
import sys
import numpy as np

def DetectCircles(image):
    houghcircles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=35,maxRadius=60)
    houghcircles = np.uint16(np.around(houghcircles))
    return houghcircles

def test():
    img = cv2.imread(sys.argv[1],0)
    img = cv2.medianBlur(img,5)
    editimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    for i in DetectCircles(img)[0,:]:
        cv2.circle(editimg,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(editimg,(i[0],i[1]),2,(0,0,255),3)
    cv2.imshow('detected circles',editimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test()
