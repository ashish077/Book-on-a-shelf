from flask import Blueprint, render_template


main = Blueprint('main', __name__)


@main.route('/search')
def login():
    return render_template('search.html')


