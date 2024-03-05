from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.books_quotes.quotes