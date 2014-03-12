import cv2


def show(image):
    '''
    Show an image without shenanigans.
    '''

    cv2.namedWindow('beatka', cv2.CV_WINDOW_AUTOSIZE)
    cv2.imshow('beatka', image)
    cv2.waitKey(0)
