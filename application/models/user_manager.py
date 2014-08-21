from application import db
from schema import User, Follow
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
	return User.query.get(user_id)
	
# make sure to change .first() to .one() later
# now impossible to make it bez of several same things
def get_user_by_email(email):
	user = User.query.filter(User.email == email).first()
	return user

def add_profile_image(user_id, filename):
	user = get_user(user_id)
	user.profile_image = filename
	db.session.commit()

def find_user(user_spelling):
	user = User.query.filter(User.username.like("%" + user_spelling + "%"))
	return user

def add_follow(follower_id, followee_id):
	follow = Follow(
		follower_id = follower_id,
		followee_id = followee_id
		)
	db.session.add(follow)
	db.session.commit()

def get_follower(follower_id):
	return User.query.get(follower_id).followees.all()

def get_followee(followee_id):
	return User.query.get(followee_id).followers.all()


	
