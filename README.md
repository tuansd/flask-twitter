
<!-- Activate the virtual environment if it is not already activated: -->
CLI; To activate enviroment:

$ . venv/scripts/activate

CLI; Create a database named twitter:

$ docker exec -i pg_container psql -c 'CREATE DATABASE twitter;'



Notice the pattern here:
<!-- CLI: cd flask/twitter -->
First we generate the migrations file with:
$ flask db migrate

<!-- CLI: $ flask db migrate -->
Then we can apply the forward migration with:
$ flask db upgrade

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


#############################################################