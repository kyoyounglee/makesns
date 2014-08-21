from application import db
from schema import Comment
from flask import session


def get_comment(comment_id):
	return Comment.query.get(comment_id)

def delete_comment(comment_id):
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