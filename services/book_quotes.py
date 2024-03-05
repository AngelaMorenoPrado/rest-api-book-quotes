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
    
def add_book_quote(quote_data):
    try:
        book_title = quote_data.get('book_title')
        quote = quote_data.get('quote')
        author = quote_data.get('author')

        quotes = Quotes(book_title=book_title, quote=quote, author=author)

        quotes.save()
        return make_response({'message': 'Successfully saved'}, 201)
    except Exception as e:
        return make_response({"message": str(e)}, 404)