import cv2
image = cv2.imread('v.jpg')
#converting image into grayscale image.
greyImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#naming the grayscale image as gray_image.png
cv2.imwrite('gray_image.png', greyImage)
cv2.imshow('Grey_image', greyImage)
cv2.waitKey(0) 
cv2.destroyAllWindows()

