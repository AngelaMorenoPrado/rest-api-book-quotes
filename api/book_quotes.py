from flask import Blueprint, request
from services.book_quotes import get_book_quotes, add_book_quote, get_book_quotes_by_author
book_quotes = Blueprint('book_quotes', __name__)

@book_quotes.route("/book-quotes", methods=["GET"])
def get_quotes():
    return get_book_quotes()

@book_quotes.route("/book-quotes/author/<author_name>", methods=["GET"])
def get_quotes_by_author(author_name):
    return get_book_quotes_by_author(author_name)

@book_quotes.route("/book-quotes", methods=["POST"])
def add_quote():
    return add_book_quote(request.json)