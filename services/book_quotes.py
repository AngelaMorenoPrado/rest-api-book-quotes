from flask import make_response
from model.book_quotes import Quotes

def get_book_quotes():
    book_quotes = []
    print('LLEG AQUI')
    try:
        print('Quotes')
        print(Quotes)

        return {"quotes": "HOLA"}
    except Exception as e:
        return make_response({'message': str(e)}, 404)