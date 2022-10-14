#How your databases is going to look

from application import db 

class Lists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tasks = db.Column(db.String())

class Todos(db.Model):
    tid = db.Column(db.Integer, primary_key=True)
    tasks = db.Column(db.String(30))
    complete = db.Column(db.Boolean, default=False)
