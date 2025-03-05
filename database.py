from flask_sqlalchemy import SQLAlchemy
import random
import string

db = SQLAlchemy()

def generate_short_code(length=6):
    """Generate a random short code for URLs"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

class URLMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, original_url):
        self.original_url = original_url
        self.short_code = generate_short_code()
