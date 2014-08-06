#-*- coding:utf-8 -*-
from application import app
from flask import render_template, url_for


@app.route('/read')
def read() :
	return render_template('read.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404