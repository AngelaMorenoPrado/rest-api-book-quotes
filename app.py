import os
from flask import Flask
from api.book_quotes import book_quotes
from mongoengine import connect

app = Flask(__name__)

app.register_blueprint(book_quotes)

connect(host=os.environ.get('MONGO_URI'))

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")