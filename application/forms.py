# Links the database with your routes, by creating input forms. 

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField

from application.models import Players, Teams 

class PlayerForm(FlaskForm):
    name = StringField("Name")
    position StringField("Position")
    fk_teamid = IntegerField("Team ID")
    submit = SubmitField("Submit")

class TeamForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")
