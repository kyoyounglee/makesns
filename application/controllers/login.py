#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request, session, redirect, url_for
from application.models.schema import *
from application import db
from application.models import user_manager



@app.route('/login', methods=['GET', 'POST'])
def login() :
	if request.method == 'POST':
		user_manager.login_check(request.form['email0'], request.form['password0'])
		session['logged_in'] = True
		session['name'] = request.form['email0']
		return redirect(url_for('wall'))
	else:
		return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404