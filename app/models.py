from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func



class User(db.Model,UserMixin):
    '''
    create the user schema for the user table
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(128))
    blog = db.relationship('Blog',lazy='dynamic')
    
    
class Blog(db.Model):
    '''
    create blog schema for the blog creation 
    '''
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment = db.relationship('Comment', lazy='dynamic')
    
class Comment(db.Model):
    '''
    create comment schema for the comment table
    '''
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    
    
class Quote:
    '''
    class for api quotes display
    '''
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote
    