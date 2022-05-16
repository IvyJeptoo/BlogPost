from flask import flash, render_template,request,redirect, url_for
from .import auth 
from ..models import User
from app import db
from flask_login import login_user, login_required,logout_user,current_user

from werkzeug.security import generate_password_hash, check_password_hash


@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('logged in successfully',category='success')
                login_user(user)
                return redirect(url_for('main.displayquote'))
                
            else:
                flash('incorrect password,try again!', category='error')
        else:
            flash('email does not exist', category='error')
    return render_template('register.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup',methods=['GET','POST'])
def signup():    
    
    if request.method == 'POST':
        email = request.form.get('email')
        username= request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        name = User.query.filter_by(username=username).first()
        if user:
            flash('email exists',category='error')        
        elif name:
            flash('username exists!',category='error')         
        elif len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error') 
        elif len(password1) < 5:
            flash('Password length should be more than 5', category='error')  
            
        else:
            new_user = User(email=email,username=username,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully', category='success')  
            return redirect(url_for('auth.login'))           
            
    
    return render_template('register.html',user=current_user)