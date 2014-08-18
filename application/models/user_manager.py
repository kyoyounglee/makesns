from application import db
from schema import *
from flask import session
from datetime import datetime

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
	user = User.query.filter(User.email == email).first()
	return user

def get_post(post_id):
	post = Post.query.filter(Post.id == post_id).first()
	return post

def get_post_5(wall_id):
	post = Post.query.filter(Post.wall_id == wall_id).order_by(db.desc(Post.edited_time)).limit(5)
	return post

def keep_getting_post_5(wall_id, num):
	post = Post.query.filter(Post.wall_id == wall_id).order_by(db.desc(Post.edited_time)).slice(num, num+5).all()
	return post

def get_comment(comment_id):
	comment = Comment.query.filter(Comment.id == comment_id).first()
	return comment

def write_timeline(form):
	post = Post(
		body = form['body'],
		created_time = datetime.now(),
		edited_time = datetime.now(),
		is_edited = False,
		is_secret = False,
		user_id = session['user_id'],
		wall_id = session['wall_id']
		)
	db.session.add(post)
	db.session.commit()

def post_delete(post_id):
	post = Post.query.get(post_id)
	db.session.delete(post)
	db.session.commit()

def comment_delete(comment_id):
	comment = Comment.query.get(comment_id)
	db.session.delete(comment)
	db.session.commit()

def write_comment(form, posts):
	comment = Comment(
		body = form['comment'],
		created_time = datetime.now(),
		post_id = posts,
		user_id = session['user_id']
		)
	db.session.add(comment)
	db.session.commit()

def post_modify(post_id, update_body):
	post = Post.query.get(post_id)
	post.body = update_body
	db.session.commit()

def add_profile_image(user_id, filename):
	user = get_user(user_id)
	user.profile_image = filename
	db.session.commit()