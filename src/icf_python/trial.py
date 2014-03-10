import cv2

img = cv2.imread('sign.ppm')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = cv2.resize(img, (200, 200), None, 0, 0, cv2.INTER_NEAREST)

img = cv2.GaussianBlur(img, (3, 3), sigmaX=0, sigmaY=0)

gradx = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
grady = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)

gradx = cv2.convertScaleAbs(gradx, alpha=1, beta=0)
grady = cv2.convertScaleAbs(grady, alpha=1, beta=0)

grad = cv2.addWeighted(gradx, 0.5, grady, 0.5, 0)

cv2.namedWindow('beatka', cv2.CV_WINDOW_AUTOSIZE)
cv2.imshow('beatka', grad)
cv2.waitKey(0)

