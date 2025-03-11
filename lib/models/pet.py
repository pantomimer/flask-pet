from lib.db import db

class Pet(db.Model):

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id')) #ownersというテーブルの
    name = db.Column(db.String(30), nullable=False)
    kind = db.Column(db.String(30), nullable=False)
    owner = db.relationship('Owner', uselist=False)

    def __init__(self, owner_id, name, kind, owner):
        self.owner_id = owner_id
        self.name = name
        self.kind = kind