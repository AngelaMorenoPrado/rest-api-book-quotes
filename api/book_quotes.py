from flask import Blueprint, request, make_response
from services.book_quotes import get_book_quotes, add_book_quote
from model.book_quotes import Quotes
book_quotes = Blueprint('book_quotes', __name__)

@book_quotes.route("/book-quotes", methods=["GET"])
def get_quotes():
    return get_book_quotes()

@book_quotes.route("/book-quotes", methods=["POST"])
def add_quote():
    return add_book_quote(request.json)