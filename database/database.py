import os
from pymongo import MongoClient

client = MongoClient(os.environ.get('MONGO_HOST'), int(os.environ.get('MONGO_PORT')))
db = client.books_quotes.quotes