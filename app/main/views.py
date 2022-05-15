from . import main
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import Blog
from app import db


@main.route('/')
@login_required
def home():
    return render_template('home.html',user=current_user)


@main.route('/quote')
@login_required
def quote():
    return render_template('quote.html')

@main.route('/blog',method=['GET','POST'])
@login_required
def blog():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')        
        user_id  = current_user._get_current_object().id
        
        new_blog = Blog(title=title,author=author, content=content, user_id=user_id)
        db.session.add(new_blog)
        db.session.commit()                   
        
    
    return render_template('blog.html')