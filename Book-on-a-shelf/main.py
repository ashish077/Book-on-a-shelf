from flask import Blueprint, render_template


main = Blueprint('main', __name__)


@main.route('/search')
def login():
    return render_template('search.html')


@main.route('/signup')
def signup():
    return render_template('signup.html')


@main.route('/signin')
def signin():
    return render_template('login.html')
