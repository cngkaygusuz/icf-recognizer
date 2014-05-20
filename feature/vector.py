import sys

def extract(integral_channels, feature_stubs):
    features = []
    for stub in feature_stubs:
        ch, p_x, p_y, he, wi = stub

        ch = integral_channels[ch]
        rect1 = ch.item(p_y, p_x)
        rect2 = ch.item(p_y, p_x+wi)
        rect3 = ch.item(p_y+he, p_x)
        rect4 = ch.item(p_y+he, p_x+wi)

        fea = rect4 + rect1 - rect2 - rect3
        features.append(fea)

    return features


def read(filepath):
    with open(filepath, "r") as fil:
        data = fil.read()
        data = data.split('\n')
        if not data[-1]:
            data.pop()

    column_ids = data.pop(0)

    vectors = {}
    for line in data:
        linesplit = line.split(',')
        picname = linesplit.pop(0)
        vectors[picname] = linesplit

    return vectors, column_ids


def write(feature_vectors, stub, output_path=None):
    if not output_path:
        stream = sys.stdout
    else:
        stream = open(output_path, 'w')

    stream.write(stub)
    stream.write('\n')

    for pic, vec in feature_vectors.items():
        vecf = ",".join(vec)
        stream.write(pic + ',' + vecf)
        stream.write('\n')

    stream.close()


def binarize(feature_vectors, class_id):
    """
    Set the given class_id to positive sample and rest negative
    Returns nothing, does it in place.
    """
    for key in feature_vectors:
        if feature_vectors[key][-1] == class_id:
            feature_vectors[key][-1] = 1
        else:
            feature_vectors[key][-1] = 0


def convert_int(feature_vectors):
    for key in feature_vectors:
        feature_vectors[key] = map(lambda el: int(el), feature_vectors[key])


def convert_str(feature_vectors):
    for key in feature_vectors:
        feature_vectors[key] = map(lambda el: str(el), feature_vectors[key])
