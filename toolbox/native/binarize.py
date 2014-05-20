import argparse

import feature.stub as stub
import feature.vector as vector


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sets given class id to positive example and rest negative")
    parser.add_argument('--data-path', '-d', required=True, help="Path for CSV file")
    parser.add_argument('--class-id', '-c', required=True, help="Positive class ID")
    parser.add_argument('--output-path', '-o', help="Output to be written")

    args = parser.parse_args()

    vecs, stub = vector.read(args.data_path)
    vector.convert_int(vecs)
    vector.binarize(vecs, 1)
    vector.convert_str(vecs)
    vector.write(vecs, stub, args.output_path)





