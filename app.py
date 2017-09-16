import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://localhost/trelloapi')
db = SQLAlchemy(app)
from models import Card, List


@app.route('/editlist/<_id>', methods=['POST'])
def edit_list(_id=None):
    """
    Modify a list with a POST request containing JSON.
    :param _id: ID of the list to modify
    :return: Success/failure
    """
    pass


@app.route('/editcard/<_id>', methods=['POST'])
def edit_card(_id=None):
    """
    Modify a card with a POST request containing JSON.
    :param _id: ID of the card to modify
    :return:
    """
    pass


@app.route('/card/<_id>', methods=['GET', 'DELETE'])
def get_card(_id=None):
    """
    API endpoint for accessing a specific card. Depending on HTTP method,
    either return card info or delete the card.
    :param _id: ID of card
    :return:
    """
    if request.method == 'DELETE':
        Card.query.filter_by(id=_id).delete()
        db.session.commit()
    elif request.method == 'GET':
        pass


@app.route('/list/<_id>', methods=['GET', 'DELETE'])
def get_list(_id=None):
    """
    API endpoint for accessing a specific list. Depending on HTTP method,
    either return list info or delete the list.
    :param _id:
    :return:
    """
    if request.method == 'DELETE':
        Card.query.filter_by(listId=_id).delete()
        List.query.filter_by(id=_id).delete()
        db.session.commit()
    elif request.method == 'GET':
        pass


@app.route('/card', methods=['POST'])
def add_card():
    """
    Add a card to the database, given properly formed JSON information.
    TODO: Error messages
    :return:
    """
    data = request.get_json()
    l = List.query.get(data.get('listId', 1))

    c = Card(data.get('title', ''),
             data.get('description', ''),
             l)
    db.session.add(c)
    db.session.commit()

    return jsonify({'status': 200})


@app.route('/list', methods=['POST'])
def add_list():
    """
    Add a list to the database, given the properly formed JSON information.
    :return:
    """
    data = request.get_json()
    lists = List.query.order_by(List.order.desc())
    o = lists[0].order+1 if lists.count() > 0 else 0
    l = List(data.get('title', ''), o)
    db.session.add(l)
    db.session.commit()

    return jsonify({'status': 200})
