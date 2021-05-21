def minkowski(ratings_1, ratings_2, r):
    """Computes the Minkowski distance.
    Both ratings_1 and rating_2 are dictionaries of the form
    {'The Strokes: 3.0, 'Slightlyt Stoopid: 2.5}
    """
    distance = 0
    commonRatings = False
    for key in ratings_1:
        if key in ratings_2:
            distance += pow(abs(ratings_1[key] - ratings_2[key]), r)
            commonRatings = True
    if commonRatings:
        return pow(distance, 1/r)
    else:
        return 0 # Indicates no ratings in common