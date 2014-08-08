#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request, url_for, redirect
from application.models.schema import *
from application import db
from application.models.user_manager import *


@app.route('/signup', methods=['GET', 'POST'])
def signup() :
	if request.method == 'POST':
		add_user(request.form)
		return redirect(url_for('login'))
	else:
		return render_template('signup.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404