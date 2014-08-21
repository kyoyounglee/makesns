from application import db
from schema import Post, User
from flask import session


def get_post(post_id):
	return Post.query.get(post_id)
# to make post_manager!!

def get_posts(wall_id, start_index):
	post = Post.query.filter(Post.wall_id == wall_id).order_by(db.desc(Post.edited_time)).offset(start_index).limit(5)
	return post

def get_post_5(wall_id):
	post = Post.query.filter(Post.wall_id == wall_id).order_by(db.desc(Post.edited_time)).limit(5)
	return post

def keep_getting_post_5(wall_id, num):
	post = Post.query.filter(Post.wall_id == wall_id).order_by(db.desc(Post.edited_time)).slice(num, num+5).all()
	return post

def write_post(form):
	post = Post(
		body = form['body'],
		# in schema.py -> default
		#created_time = datetime.now(),
		#edited_time = datetime.now(),


		# '0' False, '1' True
		is_edited = '0',
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


def post_modify(post_id, update_body):
	post = Post.query.get(post_id)
	post.body = update_body
	db.session.commit()


def get_newsfeed_posts(lists, num):
	post = Post.query.filter(Post.user_id.in_(lists) | Post.wall_id.in_(lists)).order_by(db.desc(Post.edited_time)).slice(num, num+5).all()
	return post

