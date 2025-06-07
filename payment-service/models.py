from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    amount = db.Column(db.Numeric(10, 2))
    status = db.Column(db.Enum('pending', 'paid', 'failed', name='status_enum'))
    payment_method = db.Column(db.String(50))
    payment_time = db.Column(db.DateTime)