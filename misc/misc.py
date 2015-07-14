#! -*- coding: UTF-8 -*-

"""
Miscellaneous helper functions.
"""

import cv2

from constants import *

def show(image):
    '''
    Show an image without shenanigans.
    '''

    cv2.namedWindow('beatka', cv2.CV_WINDOW_AUTOSIZE)
    cv2.imshow('beatka', image)
    cv2.waitKey(0)


def get_class(class_no):
    """
    Get the superclass of a traffic sign class
    :param class_no: Number of the class.
    :return: Number of the superclass.
    """

    if class_no in PROHIBITORY:
        return PROHIBITORY_CLASS
    elif class_no in MANDATORY:
        return MANDATORY_CLASS
    elif class_no in DANGER:
        return DANGER_CLASS
    else:
        return OTHER_CLASS


def slide(image, initial_size, step_size, scaling_factor, scaling_iteration):
    """
    A sliding window implementation.

    :param image: The image to be traversed.
    :param initial_size: Initial size of the sliding window rectangle.
    :param step_size: How many pixels to be skipped in each step, in pixels.
    :param scaling_factor: Scale the rectangle by factor of this after the window fully traverses the image.
    :param scaling_iteration: Do the aforementioned scaling this times.
    :returns Generated subimages.
    """
    dim_y, dim_x = image.shape[0], image.shape[1]
    size_x, size_y = initial_size

    for i in range(scaling_factor+1):
        iter_x = dim_x / step_size[1]
        iter_y = dim_y / step_size[0]

        for y in range(iter_y):
            point_y = y * step_size[0]
            for x in range(iter_x):
                point_x = x * step_size[1]
                subimg = image[point_y:point_y+size_y,
                               point_x:point_x+size_x]
                yield subimg
