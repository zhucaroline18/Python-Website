from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path 
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'something' ## secret key for the app 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # where database is located will store it in the webstie folder
    db.init_app(app) #take database and tell it we're using flask 

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/') #whatever is in prefix will be the prefix of the URL 

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app) #tells login manager which app we're using 

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #tells flask how we get a user, looking for primary key, check it's equal to whatever we pass 

    return app #created flask application, initialized secret key, returned it form the function 

    
def create_database(app):
#check if database exists 
    if not path.exists('website/ + DB_NAME'):
        db.create_all(app=app)
        print('Created Database!')