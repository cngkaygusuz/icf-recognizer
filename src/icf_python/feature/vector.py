import stub


def calculate_features(integral_channels, feature_stubs):
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