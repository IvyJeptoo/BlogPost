from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DB_NAME = "blog.db"

def  create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'savy'
    app.config['SQALCHEMY_DATABASE_URI'] = F'sqlite:///{DB_NAME}'
    db.init_app(app)
    
      
    from .main import main
    from .auth import auth
    
    
    app.register_blueprint(main)
    app.register_blueprint(auth)
    
    return app
