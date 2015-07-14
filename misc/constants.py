#! -*- coding: UTF-8 -*-
"""
Definitions of constant values.
"""

# Height and Width for pre-resizing of the image.
ISOLATED_DIM_X = 60
ISOLATED_DIM_Y = 60

# The IJCNN 2013 dataset is consisting of 41 distinct traffic sign types.
# These 41 classes are merged into 3 superclasses as described in [2], namely:
#   * Prohibitory: Round, white inner, red rim.
#   * Danger: (up) trianguler, white inner, red rim.
#   * Mandatory: Round, blue inner, white symbols.
# Note that not all of these classes are binned.
PROHIBITORY = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 15, 16]
MANDATORY = [33, 34, 35, 36, 37, 38, 39, 40]
DANGER = [11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

# Enumeration of superclasses.
PROHIBITORY_CLASS = 1
MANDATORY_CLASS = 2
DANGER_CLASS = 3
OTHER_CLASS = 0

