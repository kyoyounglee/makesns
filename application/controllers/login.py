#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request, session, redirect, url_for
from application.models.schema import *
from application import db
from application.models import user_manager



@app.route('/login', methods=['GET', 'POST'])
def login() :
	if request.method == 'POST':

		email = request.form['email0']
		password = request.form['password0']
		login = user_manager.login_check(email, password)

		if login :
			session['logged_in'] = True
			# session['name'] = uuser_manager.get_user_by_email(email).username
			return redirect(url_for('wall'))

		else :
			session['logged_in'] = False
			return render_template('login.html')

	else:
		return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404