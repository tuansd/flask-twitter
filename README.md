
Run Flask:
$ flask run

<!-- Activate the virtual environment if it is not already activated: -->
CLI; To activate enviroment:

$ . venv/scripts/activate

run docker image
$ docker compose up -d

CLI; Create a database named twitter:

$ docker exec -i pg_container psql -c 'CREATE DATABASE twitter;'



Notice the pattern here:
<!-- CLI: cd flask/twitter -->
First we generate the migrations file with:
$ flask db migrate

<!-- CLI: $ flask db migrate -->
Then we can apply the forward migration with:
$ flask db upgrade

To reset the database

$ cd flask
$ python seed.py
Create variable for enviroment:
$ export FLASK_ENV=development

Run Flask:
$ flask run

<!-- models.py -->
#######################################################
<!-- -->
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    tweets = db.relationship('Tweet', backref='user', cascade="all,delete")


likes_table = db.Table(
    'likes',
    db.Column(
        'user_id', db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True
    ),

    db.Column(
        'tweet_id', db.Integer,
        db.ForeignKey('tweets.id'),
        primary_key=True
    ),

    db.Column(
        'created_at', db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
)


class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(280), nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    liking_users = db.relationship(
        'User', secondary=likes_table,
        lazy='subquery',
        backref=db.backref('liked_tweets', lazy=True)
    )

    def __init__(self, content: str, user_id: int):
        self.content = content
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'user_id': self.user_id
        }


#############################################################
% <!-- -->
tweets.py
######################################################


from flask import Blueprint, jsonify, abort, request
from ..models import Tweet, User, db

bp = Blueprint('tweets', __name__, url_prefix='/tweets')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    tweets = Tweet.query.all()  # ORM performs SELECT query
    result = []
    for t in tweets:
        result.append(t.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response

#######################################################

users.py
#########################################################
from flask import Blueprint

bp = Blueprint('users', __name__, url_prefix='/users')

#######################################################
