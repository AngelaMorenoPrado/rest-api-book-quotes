from flask import Blueprint, request, make_response
from services.book_quotes import get_book_quotes
from model.book_quotes import Quotes
book_quotes = Blueprint('book_quotes', __name__)

@book_quotes.route("/book-quotes", methods=["GET"])
def get_quotes():
    quotes = []
    return get_book_quotes()

@book_quotes.route("/book-quotes", methods=["POST"])
def add_quote():
    try:
        quote_data = request.json

        book_title = quote_data.get('book_title')
        quote = quote_data.get('quote')
        author = quote_data.get('author')

        quotes = Quotes(book_title=book_title, quote=quote, author=author)

        quotes.save()
        return make_response({'message': 'Successfully saved'}, 201)
    except Exception as e:
        return make_response({'message': str(e)}, 404)