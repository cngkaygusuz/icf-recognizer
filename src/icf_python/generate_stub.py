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
    parser.add_argument('--seed-value', '-s')
    parser.add_argument('--output', '-o')

    args = parser.parse_args()


