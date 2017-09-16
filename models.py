from app import db


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    order = db.Column(db.Integer)

    def __init__(self, title, order):
        self.title = title
        self.order = order


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    description = db.Column(db.String(500))
    listId = db.Column(db.Integer, db.ForeignKey('list.id'))
    list = db.relationship('List', backref=db.backref('cards', lazy='dynamic'))

    def __init__(self, title, description, lst):
        self.title = title
        self.description = description
        self.list = lst
