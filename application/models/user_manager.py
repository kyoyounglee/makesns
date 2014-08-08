from application import db
from schema import *
from flask import session

def add_user(data):
	user = User(
		email = data['email'],
		username = data['name'],
		password = db.func.md5(data['password']),
		phone = data['mobile'],
		gender = data['gender'],
		birthday = data['birthday']
		)
	db.session.add(user)
	db.session.commit()

def login_check(email, password):
	return User.query.filter(User.email == email, User.password == db.func.md5(password)).count() != 0

def get_user(user_id):
	user = User.query.get(user_id)
	return user

def get_user_by_email(email):
	user = User.query.filter(User.email == email).all()
	return user