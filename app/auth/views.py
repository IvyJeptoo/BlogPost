from flask import flash, render_template,request,redirect, url_for
from .import auth 
from ..models import User
from app import db

from werkzeug.security import generate_password_hash, check_password_hash


@auth.route('/login',methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template('register.html')

@auth.route('/logout')
def logout():
    return "logout"

@auth.route('/signup',methods=['GET','POST'])
def signup():
    
    if request.method == 'POST':
        email = request.form.get('email')
        username= request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error') 
        elif len(password1) < 5:
            flash('Password length sshould be more than 5', category='error')  
            
        else:
            new_user = User(email=email,username=username,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully', category='success')  
            return redirect(url_for('main.home'))           
            
    
    return render_template('register.html')