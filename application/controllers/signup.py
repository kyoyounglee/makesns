#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request, url_for, redirect
from application.models.schema import *
from application import db
from application.models.user_manager import *
from flask.ext.wtf import Form
from wtforms import (
	StringField,
	PasswordField,
	SelectField,
	IntegerField
)
from wtforms.fields.html5 import DateField
from wtforms import validators


class UserForm(Form):
	name = StringField(
		u'name',
		[
			validators.data_required(message=u'please enter name')
		],
		description = {'placeholder':u'please enter name'}
		)
	email = StringField(
		u'email',
		[
			validators.data_required(message=u'please enter email'),
			validators.Email(message=u'user email form')
		],
		description = {'placeholder':u'likelion@gmail.com'}
	)
	password = PasswordField(
		u'password',
		[
			validators.data_required(message=u'please enter password'),
			validators.Length(min=8, max=20, message=u'please enter password 8 to 20')
		],
		description = {'placeholder':u'oooooooo'}
		)
	confirm = PasswordField(
		u'confirm password',
		[
			validators.data_required(message=u'please enter password again'),
			validators.EqualTo('password', message=u'please enter the same password')
		],
		description = {'placeholder': u'oooooooo'}
		)
	gender = SelectField(
		u'gender',
		choices=[
					('M', 'male'),
					('F', 'female')
				]
		)
	birthday = DateField(
		u'birthday',
		format = '%Y-%m-%d'
		)
	mobile = IntegerField(
		u'mobile',
		description = {'placeholder':u'please enter your mobile number'}
		)


@app.route('/signup', methods=['GET', 'POST'])
def signup() :
	form = UserForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			add_user(form.data)
			return redirect(url_for('login'))
		else :
			signup_error = "try again"
			return render_template('signup.html', form=form, signup_error=signup_error)
	else:
		return render_template('signup.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404