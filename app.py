from flask import Flask
from api.book_quotes import book_quotes

app = Flask(__name__)

app.register_blueprint(book_quotes)