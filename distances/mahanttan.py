def manhattan(rating_1, rating_2):
    """Computes the Man    hattan distance"""
    distance = 0
    for key in rating_1:
        if key in rating_2:
            distance += abs(rating_1[key] - rating_2[key])
    return distance
 