import json 
import orjson

# load ratings json
ratings_file_path = 'ratings.json'
ratings_file_opened = open(ratings_file_path, 'r')
ratings = json.load(ratings_file_opened)
ratings_file_opened.close()

# load books json
books_file_path = 'books.json'
books_file_opened = open(books_file_path, 'r')
books = json.load(books_file_opened)
books_file_opened.close()

book_ids = books.keys()
copy_ratings = ratings.copy()


new_ratings = {}
for user_id, ratings_values in ratings.items():
    print(user_id, ratings_values)
    # _books_keys = ratings_values.keys()
    new_ratings_values = {}
    for key, value in ratings_values.items():
        if (key in book_ids) and (value != 0):
            new_ratings_values[key] = value
        else:
            print(key, 'Not found')
            print('Deleting...')
            #del ratings_values[_books_keys]
            print('Deleted')      
    if len(new_ratings_values) > 0:
        new_ratings[user_id] = new_ratings_values


b = orjson.dumps(new_ratings, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
f = open("new_ratings_2.json", "wb")
f.write(b)
f.close()