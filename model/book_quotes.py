from mongoengine import Document, StringField

class Quotes(Document):
    book_title = StringField(required=True, max_length=256)
    quote = StringField(required=True, max_length=3000)
    author = StringField(required=True, max_length=256)