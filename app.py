from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

login = LoginManager(app)
login.login_view = 'login'

# Import models here to ensure they are known to SQLAlchemy
# It's important to import models before creating the database tables
# Import models after initializing db to avoid circular imports
from models import User, Post
#db.init_app(app)     Initialize SQLAlchemy with the Flask app
#csrf.init_app(app)  # Initialize CSRF protection

# It's crucial to import routes after the database tables are created
# and after the models are imported
# Import routes at the end to avoid circular imports
import routes

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
