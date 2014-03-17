#!/usr/bin/python
import argparse

import cv2

from util.constants import *
import feature.stub as stub
import feature.vector as vector
import util.gradient as grad


def single(image, vector_stub):
    image = cv2.resize(image, (ISOLATED_DIM_X, ISOLATED_DIM_Y), None, 0, 0, cv2.INTER_CUBIC)
    chan = grad.get_channels(image)
    int_chan = grad.get_integral_channels(chan)
    feats = vector.extract(int_chan, vector_stub)
    return feats


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract features from a single image file given the vector stub.')
    parser.add_argument('--vector-stub-path', '-v', required=True, help='Path of the vec file containing vector stub.')
    parser.add_argument('--image-path', '-i', required=True, help='Path of the image.')
    args = parser.parse_args()

    img = cv2.imread(args.image_path)
    vec_stu = stub.read(args.vector_stub_path)

    feats = single(img, vec_stu)
    print feats