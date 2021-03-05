from sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    name = db.Column(db.String(20))
