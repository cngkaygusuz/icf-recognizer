from icf_python.util.constants import *
import random

CHANNEL_COUNT = 10
UNIQUE_FEATURE_COUNT = 10

MAX_SIZE = 30
MIN_SIZE = 5

COLLISION_LIMIT = 500

# Description of feature vector:
#   Channel Number
#   X coordinate of upper left point of the box
#   Y coordinate of upper left point of the box
#   Height
#   Width


def generate_canditate_features():
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
        elif features == UNIQUE_FEATURE_COUNT:
            break

    return feature_dict


def read_feature_vector(filename):
    with open(filename, 'r') as fil:
        data = fil.read()
        data = data.split('\n')
        data = map(lambda it: it.split(' '), data)
    return data


def write_feature_vector(feature_dict, filename):
    with open(filename, 'w') as fil:
        keys = feature_dict.keys()
        for key in keys:
            fea = '%s %s %s %s %s\n' % (key[0], key[1], key[2], key[3], key[4])
            fil.write(fea)


if __name__ == '__main__':
    f = generate_canditate_features()
    write_feature_vector(f, 'canditate.vec')
    fvec = read_feature_vector('canditate.vec')
    print fvec
