#-*- coding:utf-8 -*-
from application import app
from flask import url_for, redirect, session
from application.models.schema import *


@app.route('/logout')
def logout() :
	session.pop('logged_in', None)
	session.pop('user_name', None)
	session.pop('user_id', None)
	return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404