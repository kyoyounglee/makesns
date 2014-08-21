#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request, session, redirect, url_for
# 플라스크 Extension 중 WTForms 실습 
from flask.ext.wtf import Form
from wtforms import (
	StringField,
	PasswordField
)
# Validator 가 Regex와 같이 얘가 유효한지 안한지 알려주는 것
from wtforms import validators
from application.models.schema import *
from application.models import user_manager


# Class로 Input으로 관리함
class UserForm(Form):
	email =  StringField(
		u'email', # label
		[
			validators.data_required(message=u'please enter email'), # validator : 여기에 필수로 하나 적어야한다는뜻, 만약에 안적었으면 이 에러메세지를 띄워준다.
			validators.Email(message=u'use email form')
		],
		description = {'placeholder':u'likelion@gmail.com'}
	)
	password = PasswordField(
		u'password',
		[
			validators.data_required(message=u'please enter password')
		],
		description = {'placeholder':u'oooooo'}
	)



@app.route('/login', methods=['GET', 'POST'])
def login() :
	form = UserForm()
	if request.method == 'POST':

		# Validator 안에서 옳은지 안 옳은지 확인해주는 if 문
		if form.validate_on_submit():
			login_success = user_manager.login_check(form.email.data, form.password.data)

			if login_success :
				user = user_manager.get_user_by_email(form.email.data)
				session['user_id'] = user.id
				session['user_name'] = user.username
				return redirect(url_for('newsfeed'))
			else:
				login_error = "wrong email or password"
				return render_template('login.html', form=form, login_error=login_error)

		else :
			return render_template('login.html', form=form)

	else:
		return render_template('login.html', form=form)



@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

