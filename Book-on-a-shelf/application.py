


from flask_session import Session
from flask import Flask, session, render_template

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db.init_app(app)

from main import main as main_blueprint
from auth import auth as auth_blueprint
# blueprint for auth routes in our app
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
app.register_blueprint(main_blueprint)
