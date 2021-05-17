import json

from pprint import pprint


def load_users():
    """Load users from json file"""
    global users 
    json_file = open('users.json')
    users = json.load(json_file)


def show_users():
    """Show users loaded"""
    print("========================================== users ==========================================")
    for user in users.keys():
        print(users[user])
    print("=============================================================================================")


def manhattan(rating1, rating2):
    """Computes thte Manhattan distance"""
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance


def computeNearestNeighbor(username, users):
    """Creates a sorted list of users based on their distance to
    username"""
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
    # sort based on distance -- closest first
    distances.sort()
    return distances


def recomnend(username, users):
    """Give list of recomendations"""
    # first find nearest neighbor 
    nearest = computeNearestNeighbor(username, users)[0][1]
    recomnendations = []
    # now find bands neighbor rated that user didn't 
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if not artist in userRatings:
            recomnendations.append((artist, neighborRatings[artist]))
    # using the fn sorted for variety - sort is more efficient
    return sorted(recomnendations,
                  key=lambda artistTuple: artistTuple[1],
                  reverse=True)


def main():
    load_users()
    show_users()

    print(manhattan(users['Hailey'], users['Veronica']))
    print(manhattan(users['Hailey'], users['Jordyn']))
    print(computeNearestNeighbor("Hailey", users))
    print(recomnend('Hailey', users))

if __name__ == "__main__":
    main()
