import argparse
import cv2

from util.misc import slide
from gen_single import single
from feature.stub import read


def negatives(image, sample_name, vector_stub, output_file):

    for i, subimg in enumerate(slide(image, (60, 60), (60, 60), 0, 0)):
        feats = single(image, vector_stub)
        feats = map(lambda it: str(it), feats)

        f_printy = "%s-%d" % (sample_name, i) + ', '.join(feats), ', -1' + '\n'
        output_file.write(f_printy)





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate negative samples from a WHOLE image.')
    parser.add_argument('--image', '-i',  required=True)
    parser.add_argument('--sample-name', '-sn')
    parser.add_argument('--vector-stub', 'v', required=True)
    parser.add_argument('--output-file', '-o')