import json 
import os

def load_data():
    """Load data from json file"""
    global books
    global ratings

    json_books_file = open('books.json', 'r')
    books = json.load(json_books_file)
    json_books_file.close()

    json_ratings_file = open('new_ratings_2.json', 'r')
    ratings = json.load(json_ratings_file)
    json_ratings_file.close()


def manhattan(rating_1, rating_2):
    """Computes the Manhattan distance"""
    distance = 0.0
    for key in rating_1:
        if key in rating_2:
            print(abs(rating_1[key] - rating_2[key]))
            distance += abs(rating_1[key] - rating_2[key])
            print('Distance', distance)
    return distance


def computeNearestNeighbor(user_id):
    """Creates a sorted list of books based on their distance to
    user_id"""
    distances = []
    for user in ratings:
        if user != user_id:
            distance = manhattan(ratings[user], ratings[user_id])
            distances.append((distance, user))
    # sort based on distance -- closest first
    distances.sort()
    return distances


def recomnend(user_id):
    """Give list of recomendations"""
    # first find nearest neighbor 
    nearest = computeNearestNeighbor(user_id)[0:5]
    recomnendations = []
    print(nearest)
    # now find bands neighbor rated that user didn't 
    # neighborRatings = users[nearest]
    # userRatings = users[user_id]
    # for artist in neighborRatings:
    #     if not artist in userRatings:
    #         recomnendations.append((artist, neighborRatings[artist]))
    # # using the fn sorted for variety - sort is more efficient
    # return sorted(recomnendations,
    #               key=lambda artistTuple: artistTuple[1],
    #               reverse=True)


def main():
    load_data()
    while True:
        user_to_search = input('Choice user to show recomendation: ')
        if user_to_search in ratings:
            recomnend(user_to_search)
    print('__Finish__')


if __name__ == "__main__":
    main()


# 