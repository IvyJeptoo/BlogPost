from . import main
from flask import render_template
from flask_login import login_required, current_user

@main.route('/')
@login_required
def home():
    return render_template('home.html',user=current_user)


@main.route('/quote')
@login_required
def quote():
    return render_template('quote.html')

@main.route('/blog')
@login_required
def blog():
    return render_template('blog.html')