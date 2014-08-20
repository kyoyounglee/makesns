#-*- coding:utf-8 -*-
from application import app
from flask import render_template, redirect, url_for, session


@app.route('/')
@app.route('/index')
def index() :
	if 'user_id' not in session:
		return redirect(url_for('login'))
	else:
		return redirect(url_for('wall'))
	#return render_template('layout.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

