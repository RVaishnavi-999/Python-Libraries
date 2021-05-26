import cv2
img = cv2.imread('v.jpg') #reading image from local directory
cv2.imwrite('renamed.jpg',img) #writing img differnt name
cv2.imshow('show',img) #display img show is printed on window
cv2.waitKey(0) #infinite time : utill pressing crtl+c it will show the img
cv2.destroyAllWindows() #close all windows
