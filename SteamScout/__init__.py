"""Initializes SteamScout with SQLAlchemy, Bcrypt, Bootstrap, Flask-Mail and LoginManager"""
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask.ext.login import LoginManager, login_user, logout_user, login_required
from flask.ext.mail import Mail
from flask.ext.bcrypt import Bcrypt


app = Flask(__name__)

app.config.from_object('config.ProductionConfig') 

db = SQLAlchemy(app)
Bootstrap(app)
flask_bcrypt = Bcrypt(app)

mail = Mail()
mail.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

# redirects users to the login view whenever they are required to be logged in.
login_manager.login_view = 'login'

from SteamScout.views import *

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
