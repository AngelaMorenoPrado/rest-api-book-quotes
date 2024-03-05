import os
from pymongo import MongoClient
import certifi

client = MongoClient(os.environ.get('MONGO_URI'), tlsCAFile=certifi.where())
db = client.books_quotes.quotes