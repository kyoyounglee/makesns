#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request, session, redirect, url_for
from application.models.schema import *

from application.models import user_manager


@app.route('/login', methods=['GET', 'POST'])
def login() :
	if request.method == 'POST':

		email = request.form['email']
		password = request.form['password']
		login_success = user_manager.login_check(email, password)

		if login_success :
			user = user_manager.get_user_by_email(email)
			session['user_id'] = user.id
			session['user_name'] = user.username

			return redirect(url_for('wall'))

		else :
			return render_template('login.html')

	else:
		return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404