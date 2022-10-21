# How your databases are going to look. 
from application import db 

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    position = db.Column(db.Boolean, default=False)
    fk_teamid = db.Column(db.Integer, db.ForeignKey('teams.id'))
