from types import new_class
from flask import Blueprint, render_template, redirect, url_for
from flask.globals import request
from flask.helpers import flash
from sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

db = SQLAlchemy()
auth = Blueprint('auth', __name__)


@auth.route('/login', method='POST')
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Username of Password Incorrect")
        return redirect(url_for('login.html'))

    return redirect(url_for('search.html'))


@auth.route('/register')
def register():

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = db.query.filter_by(email=email).first()

    if user:
        flash("User Alredy Exist.")
        return redirect(url_for('register.html'))
    else:
        new_user = User(name=name, email=email, password=generate_password_hash(
            password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login.html'))


@auth.route('/logout')
def logout():
    return redirect(url_for('logout.html'))
