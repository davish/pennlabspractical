from app import db


class UpdateMixin():
    def update(self, newdata):
        for key, value in newdata.items():
            setattr(self, key, value)


class List(db.Model, UpdateMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    order = db.Column(db.Integer)

    def __init__(self, title, order):
        self.title = title
        self.order = order

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'order': self.order
        }

    def serialize_nested(self):
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
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'listId': self.listId
        }
