from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    status = db.Column(db.Enum('created', 'processed', 'completed', name='order_status_enum'))
    payment_status = db.Column(db.Enum('pending', 'paid', 'failed', name='order_payment_status_enum'))
    order_time = db.Column(db.DateTime)