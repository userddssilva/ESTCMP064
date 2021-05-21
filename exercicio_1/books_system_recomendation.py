import sys
sys.path.append('../')

import json 
import os

from distances import manhattan

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


def computeNearestNeighbor(user_id):
    """Creates a sorted list of books based on their distance to
    user_id"""
    distances = []
    for user in ratings:
        if user != user_id:
            distance = manhattan(ratings[user], ratings[user_id])
            distances.append((distance, user))
    return sorted(distances)


def recomnend(user_id):
    """Give list of recomendations"""
    # 5 first neighbors
    nearest = computeNearestNeighbor(user_id)[0:5]
    recomnendations = []
    
    # books of 5 firsts to recomnend
    for _, neighbor in nearest:
        for book_id in ratings[neighbor]:
            recomnendations.append(books[book_id])

    if len(recomnendations) >= 10:
        return recomnendations[0:9]
    else:
        return recomnendations


def main():
    load_data()
    while True:
        user_to_search = input('Choice user to show recomendation: ')
        if user_to_search in ratings:
            recomendations = recomnend(user_to_search)
            print('============= Recommended books ===============')
            for book in recomendations:
                print(book)
            print('===============================================')
        else:
            print('User deleted from database')


if __name__ == "__main__":
    main()