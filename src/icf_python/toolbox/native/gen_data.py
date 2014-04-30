#!/usr/bin/python
from argparse import ArgumentParser
import os

import cv2

from icf_python.toolbox.native.gen_single import single
from util.misc import get_class
import feature.stub as stub
import util.gradient as grad


TRAINING_DATASET_PATH = '/home/cengiz/Desktop/cengizdata/junior-proje/dataset/detection-training'


def generate_from_training(output_filepath, vector_stub_path):
    dir_structure = list(os.walk(TRAINING_DATASET_PATH))
    dir_structure.pop(0)  # first element is useless

    vec_stub = stub.read(vector_stub_path)

    with open(output_filepath, 'w') as output:
        output.write('name,')

        for s in vec_stub:
            tmp = "({} {} {} {} {}),".format(*s)
            output.write(tmp)

        output.write('class')
        output.write('\n')

        for root, dirs, files in dir_structure:
            dir_no = root[-2:]
            class_no = int(dir_no)
            class_no = get_class(class_no)

            for file in files:
                img = cv2.imread('%s/%s' % (root, file))

                features = single(img, vec_stub)
                features = map(lambda it: str(it), features)

                features_printy = '%s-%s, ' % (dir_no, file) + ', '.join(features) + ', %d' % class_no + '\n'
                output.write(features_printy)


def generate_negatives(image, output_filepath):
    with open(output_filepath, 'w') as output:
        chan = grad.get_channels(image)
        int_chan = grad.get_integral_channels(chan)


if __name__ == '__main__':
    parser = ArgumentParser(description='Generate raw data using a vector stub.')
    parser.add_argument('--output-filepath', '-o', help='path for the output file.', required=True)
    parser.add_argument('--vector-stub-filepath', '-v', help='path for the stub file.', required=True)

    args = parser.parse_args()

    generate_from_training(args.output_filepath, args.vector_stub_filepath)


