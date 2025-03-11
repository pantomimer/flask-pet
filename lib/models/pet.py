from lib.db import db

class Pet(db.Model):

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id')) #ownersというテーブルの
    name = db.Column(db.String(30), nullable=False)
    shurui = db.Column(db.String(30), nullable=False)
    owner = db.relationship('Owner', uselist=False)

    def __init__(self, owner_id, name, shurui, owner):
        self.owner_id = owner_id
        self.name = name
        self.shurui = shurui