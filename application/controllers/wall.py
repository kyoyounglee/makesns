#-*- coding:utf-8 -*-
from application import app
from flask import render_template, url_for, redirect, session, request
from application.models.user_manager import *


@app.route('/wall', defaults={'wall_id':0}, methods=['GET', 'POST'])
@app.route('/timeline/<int:wall_id>', methods=['GET', 'POST'])
def wall(wall_id) :
	if request.method == 'POST' :

		if session['logged_in'] != True :
			return redirect(url_for('login'))

		if wall_id == 0:
			wall_id = session['user_id']

		session['wall_id'] = wall_id
		session['wall_name'] = get_user(wall_id)[0].username

		return render_template('wall.html')

	return render_template('wall.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404