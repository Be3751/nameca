from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Card(db.Model):
    __tablename__ = 'cards'
    imgname = db.Column(db.String(100), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    furigana = db.Column(db.String(30), nullable=False)
    birthday = db.Column(db.String(10), nullable=False)
    favorite = db.Column(db.String(30), nullable=False)
    skills = db.Column(db.String(30), nullable=False)

def init_db(app):
    db.init_app(app)
    db.drop_all()
    db.create_all()

def get_all():
    return Card.query.order_by(Card.id).all()

def insert(card_info):
    model = Card(
                imgname=card_info['imgname'],
                name=card_info['name'], 
                furigana=card_info['furigana'],
                birthday=card_info['birthday'],
                favorite=card_info['favorite'],
                skills=card_info['skills']
            )
    db.session.add(model)
    db.session.commit()