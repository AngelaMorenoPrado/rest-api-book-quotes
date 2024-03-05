from json import dumps
from flask import make_response, jsonify
from model.book_quotes import Quotes
from database.database import db
from bson.json_util import dumps

def get_book_quotes():
    try:
        return dumps(db.find())
    except Exception as e:
        return make_response({'message': str(e)}, 404)
    
def add_book_quote(quote_data):
    try:
        book_title = quote_data.get('book_title')
        quote = quote_data.get('quote')
        author = quote_data.get('author')

        quotes = Quotes(book_title=book_title, quote=quote, author=author)
        quotes_dict = quotes.to_mongo().to_dict()

        db.insert_one(quotes_dict)
        return make_response({'message': 'Successfully saved'}, 201)
    except Exception as e:
        return make_response({"message": str(e)}, 404)