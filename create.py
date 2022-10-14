from application import db

#create database
db.drop_all()
db.create_all()