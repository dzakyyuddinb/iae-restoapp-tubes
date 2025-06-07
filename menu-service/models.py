from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Menu(db.Model):
    __tablename__ = 'menus'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    price = db.Column(db.Numeric(10, 2))
    stock = db.Column(db.Integer)