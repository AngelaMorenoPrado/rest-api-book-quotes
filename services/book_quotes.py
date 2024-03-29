from json import dumps
from flask import make_response
from model.book_quotes import Quotes
from database.database import db
from bson.json_util import dumps

def get_book_quotes():
    # Returns up to 15 random quotes
    try:
        pipeline = [
            {"$sample": {"size": 15}},
            {"$project": {"book_title": 1, "quote": 1, "author": 1, "_id": 0}}
        ]

        return dumps(db.aggregate(pipeline))
    except Exception as e:
        return make_response({'message': str(e)}, 404)
    
def get_book_quotes_by_author(author_name):
    try: 
        pipeline = [
            {"$match": {"author": author_name}},
            {"$sample": {"size": 15}},
            {"$project": {"book_title": 1, "quote": 1, "author": 1, "_id": 0}}
        ]

        return dumps(db.aggregate(pipeline))
    except Exception as e:
        return make_response({'message': str(e)}, 404)
    
def get_book_quotes_by_title(book_title):
    try: 
        pipeline = [
            {"$match": {"book_title": book_title}},
            {"$sample": {"size": 15}},
            {"$project": {"book_title": 1, "quote": 1, "author": 1, "_id": 0}}
        ]

        return dumps(db.aggregate(pipeline))
    except Exception as e:
        return make_response({'message': str(e)}, 404)

def add_book_quote(quote_data):
    try:
        quotes = Quotes(**quote_data)
        quotes.validate()
        quotes_dict = quotes.to_mongo().to_dict()

        db.insert_one(quotes_dict)
        return make_response({'message': 'Successfully saved'}, 201)
    except Exception as e:
        return make_response({"message": str(e)}, 404)