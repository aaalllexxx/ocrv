from settings import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    session_id = db.Column(db.String(120))
    text_id = db.Column(db.Integer)
    recent_texts = db.Column(db.String(1024))

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password
        self.text_id = 0
        self.recent_texts = "[]"

    def __repr__(self):
        return '<User %r>' % self.id
