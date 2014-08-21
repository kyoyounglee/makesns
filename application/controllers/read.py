#-*- coding:utf-8 -*-
from application import app
from flask import render_template, url_for, request, session
from application.models.user_manager import *
from application.models.post_manager import *


@app.route('/read/<int:wall_id>/<int:id>', methods=['GET', 'POST'])
def read(wall_id, id) :
	post = get_post(id)
	wall_owner = get_user(wall_id)
	posts = wall_owner.wall_posts
	comments = post.comments
	session['post_id'] = id
	if request.method == 'POST':
		write_comment(request.form, id)
	return render_template('read.html', post = post, comments = comments, post_id=session['post_id'])



@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404