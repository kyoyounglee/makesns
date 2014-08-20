#-*- coding:utf-8 -*-
from application import app
from flask import render_template, url_for, session, request, redirect
from application.models.post_manager import *

# 로그인 안 되어 있으면 로그인페이지로 리턴
@app.route('/write', methods=['GET', 'POST'])
def write() :
	if 'user_id' not in session:
		return redirect(url_for('login'))
	if request.method == 'POST':
		write_post(request.form)
		return redirect(url_for('wall', wall_id=session['wall_id']))
	return render_template('write.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404