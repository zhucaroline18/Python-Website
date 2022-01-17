#separate app so don't have all views in one file but multiple files 

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash #how to secure password so not stored in plain text, convert password into something more secure 
from . import db

from flask_login import login_user, login_required, logout_user, current_user
#hash has no function 

#now set up blueprint for flask application 
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required #from our imports, only logout when you're logged in 
def logout():
    logout_user() 
    return redirect(url_for('auth.login')) #reutrn to login page 

@auth.route('/sign-up', methods = ['GET', 'POST'])
# basically the website and then with this after will be the url to the sign up page that displays signup
def sign_up():
    if request.method == 'POST':
        #retrieving information from the form 
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email = email).first()
        if user:
            flash('Email already exists', category= 'error')
        # making validity checks on given data 
        #flask can flash a method on teh screen 
        elif len(email)<4:
            flash('Email must be greater than 3 characters.', category = 'error')
        elif len(first_name)<2:
            flash('First name must be greater than 1 character.', category = 'error')
        elif password1!=password2:
            flash('Passwords don\'t match', category = 'error')
        elif len(password1)<7:
            flash('Password must be at least 7 characters.', category = 'error')
        else:
            #add user to database
            new_user = User(email = email, first_name = first_name, password = generate_password_hash(password1, method = 'sha256'), amount_completed = 0)
            
            db.session.add(new_user)
            #commit to the database and add changes
            db.session.commit()
            login_user(new_user, remember = True)
            flash('Account created!', category = 'success')
            return redirect(url_for('views.home')) #blueprint name and function name 
            
    return render_template("sign_up.html", user = current_user)
            

    return render_template("sign_up.html")