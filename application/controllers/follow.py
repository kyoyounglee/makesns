from application import app
from flask import render_template, redirect, url_for, request, session
from application.models.user_manager import *

@app.route('/follow', defaults={'follower_id':0, 'followee_id':0}, methods=['GET', 'POST'])
@app.route('/follow/<int:follower_id>/<int:followee_id>', methods=['GET', 'POST'])
def follow(follower_id, followee_id):
	followers = get_follower(session['user_id'])
	followees = get_followee(session['user_id'])
	if request.method == 'POST':
		key = request.form['key']
		search_user = find_user(key)
		return render_template('follow_list.html', find_user = search_user)
	else:
		if follower_id==0 and followee_id==0:
			return render_template('follow.html', followers=followers, followees=followees)
		else:
			add_follow(follower_id, followee_id)
	return render_template('follow.html', followers=followers, followees=followees)