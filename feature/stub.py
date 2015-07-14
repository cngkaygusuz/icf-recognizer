#! -*- coding: UTF-8 -*-

"""
A feature stub can be thought as the "blueprint" of the features.

Recall that one particular feature dimension is described as:
    * Channel Number
    * X coordinate of upperleft point of the box
    * Y coordinate of upperleft point of the box
    * Height
    * Width

A feature is essentially a 5-tuple, carrying the information given above. This module is concerned with generation,
serialization and deserialization of these feature tuples.
"""

from misc.constants import *
import random

CHANNEL_COUNT = 10
UNIQUE_FEATURE_COUNT = 10

MAX_SIZE = 30
MIN_SIZE = 5

COLLISION_LIMIT = 500


def generate(seed_value=None, uniq_features=None):
    """
    Generates feature stubs.

    :param seed_value: Seed value for the random number generation. May be used for reproducible feature stubs.
    :param uniq_features: Number of unique features to be generated.
    :return: Generated feature stub.
    """
    if not uniq_features:
        uniq_features = UNIQUE_FEATURE_COUNT

    if seed_value:
        random.seed(seed_value)

    feature_dict = {}
    features = 0
    failures = 0

    while True:
        ch = random.randint(0, CHANNEL_COUNT - 1)
        he = random.randint(5, 30)
        wi = random.randint(5, 30)
        p_x = random.randint(0, ISOLATED_DIM_X - wi)
        p_y = random.randint(0, ISOLATED_DIM_Y - he)

        tup = (ch, p_x, p_y, he, wi)

        if not feature_dict.get(tup):
            feature_dict[tup] = True
            features += 1
        else:
            failures += 1

        if failures == COLLISION_LIMIT:
            raise Exception('Collision limit reached')
        elif features == uniq_features:
            break

    return feature_dict.keys()


def read(filename):
    """
    Reads the feature stub file.
    :param filename: Name of the file to be read.
    :return: Read feature stub.
    """
    with open(filename, 'r') as fil:
        data = fil.read()
        data = data.split('\n')
        data.pop()

        data = map(lambda it: it.split(' '), data)
        data = map(lambda it: map(lambda el: int(el), it), data)
    return data


def write(stubs, filename):
    """
    Writes the stub set to file.

    :param stubs:       The stub set.
    :param filename:    Name of the file to be written.
    :return: Nothing.
    """
    with open(filename, 'w') as fil:
        for stu in stubs:
            fea = '%s %s %s %s %s\n' % (stu[0], stu[1], stu[2], stu[3], stu[4])
            fil.write(fea)


if __name__ == '__main__':
    f = generate()
    write(f, 'canditate.vec')
    fvec = read('canditate.vec')
    print fvec
