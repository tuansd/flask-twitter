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
