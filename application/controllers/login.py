#-*- coding:utf-8 -*-
from application import app
from flask import render_template


@app.route('/login')
def login() :
	return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404