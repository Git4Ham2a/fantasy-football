from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, template_folder="templates")
# Sets up your database. We are using SQLAlchemy's sqlite. 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql:3306/flask-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Secrets'
db = SQLAlchemy(app)
# imports the routes.py from application. 
from application import routes
