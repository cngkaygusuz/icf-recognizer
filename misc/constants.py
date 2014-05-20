ISOLATED_DIM_X = 60
ISOLATED_DIM_Y = 60

PROHIBITORY = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 15, 16]
MANDATORY = [33, 34, 35, 36, 37, 38, 39, 40]
DANGER = [11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

PROHIBITORY_CLASS = 1
MANDATORY_CLASS = 2
DANGER_CLASS = 3
OTHER_CLASS = 0


def get_class(class_no):
    if class_no in PROHIBITORY:
        return PROHIBITORY_CLASS
    elif class_no in MANDATORY:
        return MANDATORY_CLASS
    elif class_no in DANGER:
        return DANGER_CLASS
    else:
        return OTHER_CLASS