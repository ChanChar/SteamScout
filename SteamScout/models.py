"""Contains the User, Games, and Preferences models to use with SQLAlchemy"""
from flask.ext.login import UserMixin
from .import db, flask_bcrypt
from datetime import datetime

# UserMixin contains the properties andmethods required by flask-login
# for our user object
class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    registered_on = db.Column(db.DateTime)
    validated = db.Column(db.Boolean, default=False)
    validated_on = db.Column(db.DateTime)

    def __init__(self, username, email, password, registered_on=None, validated=False, validated_on=None):
        self.username = username
        self.email = email
        self.password = flask_bcrypt.generate_password_hash(password)
        if registered_on == None:
            registered_on = datetime.now()
        self.registered_on = registered_on
        self.validated = validated
        self.validated_on = validated_on

    def __repr__(self):
        return '<ID: {} name: {}>'.format(self.id, self.username)


class Preferences(db.Model):
    __tablename__ = 'preferences'
    preference_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    game_id = db.Column(db.Integer)
    game_name = db.Column(db.String, unique=False)
    threshold_amount = db.Column(db.Float)
    notification_sent = db.Column(db.Boolean, default=False)

    def __init__(self, user_id, game_id, game_name, threshold_amount, notification_sent=False):
        self.user_id = user_id
        self.game_id = game_id
        self.game_name = game_name
        self.threshold_amount = threshold_amount
        self.notification_sent = notification_sent

    def __repr__(self):
        printable = 'UserID: {} -- Game: {} -- Threshold: {}>'
        return printable.format(self.user_id, self.game_name, self.threshold_amount)

class Games(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, unique=True)
    game_name = db.Column(db.String, unique=True)

    def __init__(self, game_id, game_name):
        self.game_id = game_id
        self.game_name = game_name

    def __repr__(self):
        return 'Game:{} -- Game ID{}'.format(self.game_name, self.game_id)
