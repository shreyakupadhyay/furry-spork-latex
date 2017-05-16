'''
Description: THis algorithm uses hough_gradient and hard coded min and max radius values.
This code doesn't give good results.

'''

import cv2
# import cv2.cv as cv
import numpy as np
import sys

img = cv2.imread(sys.argv[1],0)
img = cv2.equalizeHist(img)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,param1=50,param2=30,minRadius=35,maxRadius=60)
print circles
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()


# import numpy as np
# import cv2
# # Create a black image
# img = np.zeros((512,512,3), np.uint8)
# # Draw a diagonal blue line with thickness of 5 px
# img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import numpy as np
# import cv2
# # Create a black image
# img = np.zeros((512,512,3), np.uint8)
# # Draw a diagonal blue line with thickness of 5 px
# cv2.line(img,(0,0),(511,511),(255,0,0),5)
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
