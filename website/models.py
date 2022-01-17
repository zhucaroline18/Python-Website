#need database model for users and one for notes/ tasks 

from . import db 
#importing from the folder the db object 
#from this package, import db 

from flask_login import UserMixin
#class we can inherit specifically for flask login- help us log users in 
from sqlalchemy.sql import func

class Note(db.Model):
    #blueprint for object in database - all notes conform to what's next
    #information will be consistent 
    id = db.Column(db.Integer, primary_key = True) #database will automatically set id for you 
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

    #one user will have many tasks 


# storing all users in schema that looks like : 
class User(db.Model, UserMixin):
    #what do we want to store
    id = db.Column(db.Integer, primary_key = True)
    #need a way to uniquely identify user so need primary key 
    email = db.Column(db.String(150), unique=True) #everyone needs different email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    amount_completed = db.Column(db.Integer)
    notes = db.relationship('Note') #list storing all different notes 
    

