import cv2                           #importing library opencv
img = cv2.imread('v.jpg')            #reading image from local directory
cv2.imwrite('renamed.jpg',img)       #writing image in different name or renaming image
cv2.imshow('show',img)               #display image, show will be printed on window
cv2.waitKey(0)                       #infinite time 
cv2.destroyAllWindows()              #close all windows.
