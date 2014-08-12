#-*- coding:utf-8 -*-
from application import app
from flask import render_template, url_for, session, request, redirect
from application.models.user_manager import *


@app.route('/write', methods=['GET', 'POST'])
def write() :
	if request.method == 'POST':
		write_timeline(request.form)
		return redirect(url_for('wall', wall_id=session['wall_id']))
	return render_template('write.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404