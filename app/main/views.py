from . import main
from flask import render_template, request, redirect, url_for, flash
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


@main.route('/blogs')
@login_required
def blogs():
    allblogs = Blog.query.all()
    return render_template('blog_display.html', allblogs=allblogs)

@main.route('/blog',methods=['GET','POST'])
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
        
        return redirect(url_for('main.blogs'))               
        
    
    return render_template('blog.html')

@main.route('/delete/<int:blog_id>', methods=['GET','POST'])
@login_required
def deleteblog(blog_id):
    blog = Blog.query.get(blog_id)
    
   
    db.session.delete(blog)
    db.session.commit()
    flash("deleted!",category='success')
    
    return redirect(url_for('main.blogs'))
        
    