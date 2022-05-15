from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

DB_NAME = "database.db"

def  create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'savy'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initializing the database
    db.init_app(app)   
    
    
    # importing blueprints 
    from .main import main
    from .auth import auth
    
    # registering blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)
    
    
    # importing models
    from .models import User,Blog, Comment
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    
    return app

def create_database(app):
    if not path.exists('app/' + DB_NAME):
        db.create_all(app=app)
        print ('Created database!')
