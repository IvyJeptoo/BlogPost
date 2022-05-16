from . import main
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import Blog, Comment
from app import db

from ..requests import get_quote


@main.route('/')
@login_required
def home():
    return render_template('home.html',user=current_user)





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
    
    blog = Blog.query.get_or_404(blog_id)
    current_user_id = current_user.id
    
    
    if current_user_id != 1:
        flash("only the blog creator can delete this blog!", category='error')  
    else:
        if blog:
            db.session.delete(blog)
            db.session.commit()
            flash("deleted!",category='success')
    
    return redirect(url_for('main.blogs'))

@main.route('/comment',methods=['GET','POST'])
@login_required
def comment():
    if request.method == 'POST':        
        content = request.form.get('content')
        nickname = request.form.get('nickname')        
        new_comment = Comment(content=content,nickname=nickname)
        
        db.session.add(new_comment)
        db.session.commit()
        print(new_comment)
        
        return redirect(url_for('main.comments')) 
    
    return render_template('comments.html')

        
@main.route('/comments')
@login_required
def comments():
    allcomments = Comment.query.all()
    print(allcomments)
    return render_template('comments.html', allcomments=allcomments)

@main.route('/remove/<int:comment_id>', methods=['GET','POST'])
@login_required
def deletecomment(comment_id):
        comment = Comment.query.get_or_404(comment_id)
    
        db.session.delete(comment)
        db.session.commit()        
        flash("comment deleted!",category='success')
        return render_template ('comments.html')
    
@main.route('/quotes')
@login_required
def displayquote():
    quote = get_quote()
    
    
    return render_template('quotesdisplay.html',quote=quote)


@main.route('/edit/<int:blog_id>', methods=['GET','POST'])
@login_required
def editblog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    current_user_id = current_user.id    
    
    if request.method == 'POST':
        if current_user_id != 1:
            flash("only the blog creator can edit this blog!", category='error')  
        else:
            if blog:
                blog.title = request.form.get('title')
                blog.author = request.form.get('author')
                blog.content = request.form.get('content')
            
                db.session.add(blog)
                db.session.commit()
            
                flash("post has been updated!", category='success')
            
                return redirect(url_for('main.blogs'))
            else:
              flash('post not found', category='error')
    else:
        blog.title = request.form.get('title')
        blog.author = request.form.get('author')
        blog.content = request.form.get('content')
        
    return render_template('edit.html')
            
        
     
    
    