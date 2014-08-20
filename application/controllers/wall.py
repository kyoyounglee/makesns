#-*- coding:utf-8 -*-
from application import app
from flask import render_template, url_for, redirect, session, request
from application.models.user_manager import *
from application.models.post_manager import *


@app.route('/timeline', defaults={'wall_id':0})
@app.route('/timeline/<int:wall_id>')
def wall(wall_id) :
	if 'user_id' not in session :
		return redirect(url_for('login'))

	if wall_id == 0:
		wall_id = session['user_id']

	wall_owner = get_user(wall_id)
	session['wall_id'] = wall_owner.id

	posts = wall_owner.wall_posts

	'''
	context = {}
	context['wall_owner'] = wall_owner
	context['posts'] = posts
	return render_template('wall.html', context = context)
	'''
	return render_template('wall.html', wall_owner=wall_owner, posts=posts)

@app.route('/ajax', methods=['POST'])
def ajax():

	posts = get_post_5(session['wall_id'])
	wall_owner = get_user(session['wall_id'])
	return render_template('wall_ajax.html', wall_owner=wall_owner, posts=posts)

@app.route('/ajax_again', methods=['GET', 'POST'])
def ajax_again():
	if request.method == 'POST':
		number = int(request.form['num'])
		wall_owner = get_user(session['wall_id'])
		posts = keep_getting_post_5(session['wall_id'], number)

		if posts == []:
			return ''

	return render_template('keep_wall_ajax.html', wall_owner=wall_owner, posts=posts)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404