#-*- coding:utf-8 -*-
from application import app
from flask import render_template, url_for, redirect, session, request
from application.models.user_manager import *
import sys
import json


@app.route('/my_wall', defaults={'wall_id':0}, methods=['GET', 'POST'])
@app.route('/timeline/<int:wall_id>', methods=['GET', 'POST'])
def wall(wall_id) :
	if not 'user_id' in session :
		return redirect(url_for('login'))

	if wall_id == 0:
		wall_id = session['user_id']

	wall_owner = get_user(wall_id)
	session['wall_id'] = wall_owner.id

	posts = wall_owner.wall_posts

	return render_template('wall.html', wall_owner=wall_owner, posts=posts)

@app.route('/ajax', methods=['GET', 'POST'])
def ajax():
	if request.method == 'POST':
		posts = get_post_5(session['wall_id'])
		wall_owner = get_user(session['wall_id'])
	return render_template('wall_ajax.html', wall_owner=wall_owner, posts=posts)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404