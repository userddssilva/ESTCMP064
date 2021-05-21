import distances

def euclidean(rating_1, rating_2):        
    """Compute the euclidean distance"""
    sum_diff = 0
    for key in rating_1:
        if key in rating_2:
            sum_diff += abs(rating_1[key] - rating_2[key]) ** 2
    distance = sqrt(sum_diff)
