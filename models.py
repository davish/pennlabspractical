from app import db


class UpdateMixin():
    """
    This mixin adds an `update` function to classes which sub-class it which allows
    easy updating from dictionaries.
    """
    def update(self, newdata):
        """
        :param newdata: dictionary of new values for the given keys (attributes)
        :return:
        """
        for key, value in newdata.items():
            if value is not None:
                setattr(self, key, value)


class List(db.Model, UpdateMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    order = db.Column(db.Integer)

    def __init__(self, title, order):
        self.title = title
        self.order = order

    def serialize(self):
        """
        :return: A JSON representation of the List for transmission via the API
        """
        return {
            'id': self.id,
            'title': self.title,
            'order': self.order
        }

    def serialize_nested(self):
        """
        `serialize_nested` is used over `serialize` to reduce the number of API calls
        from one-per-list to just 1 for every list.
        :return: A JSON representation of the List with all of its constituent Cards
        """
        r = self.serialize()
        r['cards'] = [c.serialize() for c in self.cards]
        return r


class Card(db.Model, UpdateMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    description = db.Column(db.String(500))
    listId = db.Column(db.Integer, db.ForeignKey('list.id'))
    list = db.relationship('List', backref=db.backref('cards', lazy='dynamic'))

    def __init__(self, title, description, lst):
        self.title = title
        self.description = description
        self.list = lst

    def serialize(self):
        """
        :return: A JSON representation of a Card
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'listId': self.listId
        }
