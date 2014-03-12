#!/usr/bin/python
import argparse

import feature.stub as stub


desc_text = '''Generate a vector stub.
A vector stub consists of 5 integers, which holds the information of:
    * Channel: Which channel to use
    * X coordinate of upper-left point of the rectangle
    * Y coordinate of upper-left point of the rectangle
    * Height
    * Width
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=desc_text)
    parser.add_argument('--seed-value', '-s', help='Value for random seed, can be any string literal')
    parser.add_argument('--output', '-o', help='Name of the output file')
    parser.add_argument('--features', '-f', help='Number of the stubs wanted')

    args = parser.parse_args()
    print args
    gsu = stub.generate(args.seed_value, args.features)

    if args.output:
        stub.write(gsu, args.output)
    else:
        for s in gsu:
            print '{} {} {} {} {}'.format(*s)
