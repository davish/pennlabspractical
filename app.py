import os

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://localhost/trelloapi')
db = SQLAlchemy(app)
from models import Card, List


def filter_dict(d, l):
    """
    Filter dictionary to only contain specific keys
    :param d: original dictionary
    :param l: list of keys to include
    :return: dictionary only containing keys in l
    """
    return {k: d[k] for k in d}


@app.route('/list/<_id>/cards', methods=['GET'])
def get_cards_from_list(_id):
    """
    Get all cards associated with the given listId.
    :param _id: list ID
    :return: list of cards
    """

    if _id == 'all':
        # If the URL accessed is '/list/all/cards', return a JSON document with
        ls = List.query.order_by(List.order.asc())
        return jsonify({'lists': [l.serialize_nested() for l in ls]})

    l = List.query.get(_id)
    if l is None:
        return jsonify({'status': 404})

    # serialize all of the cards to be passed into JSON
    return jsonify({'result': 200, 'cards': [c.serialize() for c in l.cards]})


@app.route('/lists', methods=['GET'])
def get_all_lists():
    """
    Return all of the lists in the database, ordered by their "order" attribute
    :return:
    """
    return jsonify({'result': 200, 'lists': [l.serialize() for l in List.query.order_by(List.order.asc())]})


@app.route('/card/<_id>', methods=['GET', 'DELETE'])
def get_card(_id=None):
    """
    API endpoint for accessing a specific card. Depending on HTTP method,
    either return card info or delete the card.
    :param _id: ID of card
    :return:
    """
    c = Card.query.get(_id)
    if c is None:
        return jsonify({'status': 404})
    if request.method == 'DELETE':
        db.session.delete(c)
        db.session.commit()
        return jsonify({'status': 200})
    elif request.method == 'GET':
        return jsonify(c.serialize().update({'status': 200}))  # return the serialized card with a status code.


@app.route('/list/<_id>', methods=['GET', 'DELETE'])
def get_list(_id=None):
    """
    API endpoint for accessing a specific list. Depending on HTTP method,
    either return list info or delete the list.
    :param _id:
    :return:
    """
    l = List.query.get(_id)
    if l is None:
        return jsonify({'status': 404})
    if request.method == 'DELETE':
        db.session.delete(l.cards)  # first delete all cards associated with the list.
        db.session.delete(l)
        db.session.commit()
        return jsonify({'status': 200})
    elif request.method == 'GET':
        return jsonify(l.serialize().update({'status': 200}))  # return the serialized list with a status code.


@app.route('/card', methods=['POST'])
def add_card():
    """
    Add a card to the database, given properly formed JSON information.
    TODO: Error messages
    :return:
    """
    data = request.get_json()
    if data is None:
        return jsonify({'status': 400, 'message': 'no JSON in request body.'})
    l = List.query.get(data.get('listId', 1))

    c = Card(data.get('title', ''),
             data.get('description', ''),
             l)
    db.session.add(c)
    db.session.commit()

    return jsonify({'status': 201})


@app.route('/list', methods=['POST'])
def add_list():
    """
    Add a list to the database, given the properly formed JSON information.
    :return:
    """
    data = request.get_json()
    if data is None:
        return jsonify({'status': 400, 'message': 'no JSON in request body.'})

    lists = List.query.order_by(List.order.desc())
    o = lists[0].order+1 if lists.count() > 0 else 0
    l = List(data.get('title', ''), o)
    db.session.add(l)
    db.session.commit()

    return jsonify({'status': 201})


@app.route('/editlist/<_id>', methods=['POST'])
def edit_list(_id=None):
    """
    Modify a list with a POST request containing JSON.
    :param _id: ID of the list to modify
    :return: Success/failure
    """
    l = List.query.get(_id)
    if l is None:
        return jsonify({'status': 404})

    data = request.get_json()
    if data is None:
        return jsonify({'status': 400, 'message': 'no JSON in request body.'})

    l.update(filter_dict(data, ['title', 'order']))
    if List.query.filter(List.order == l.order, List.id != l.id).count() > 0:
        return jsonify({'status': 400, 'message': 'another list exists with this order already.'})

    db.session.commit()
    return jsonify({'status': 200})


@app.route('/editcard/<_id>', methods=['POST'])
def edit_card(_id=None):
    """
    Modify a card with a POST request containing JSON.
    :param _id: ID of the card to modify
    :return:
    """
    c = Card.query.get(_id)
    if c is None:
        return jsonify({'status': 404})

    data = request.get_json()
    if data is None:
        return jsonify({'status': 400, 'message': 'no JSON in request body.'})

    c.update(filter_dict(data, ['title', 'description']))
    db.session.commit()
    return jsonify({'status': 200})


@app.route('/form', methods=['GET'])
def show_form():
    return render_template('input.html')

if __name__ == '__main__':
    app.run()
