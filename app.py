from flask import Flask
from api.book_quotes import book_quotes

app = Flask(__name__)

app.register_blueprint(book_quotes)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")